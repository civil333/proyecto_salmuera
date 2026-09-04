#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Captura un correo entrante de BW Water o Bureau Veritas en CORREOS/_RECIBIDOS/.

Recibe por stdin (o por --json ARCHIVO) el payload extraido de Outlook Web y
escribe la carpeta canonica del mensaje con su _correo.md. Es idempotente: si el
mensaje_id ya esta capturado, no hace nada y sale con codigo 0.

La convencion completa vive en el _LEEME.md de la carpeta padre. Lo esencial:
  - Domicilio unico del correo recibido; los adjuntos con destino propio se
    mueven alla y el _correo.md deja el puntero.
  - Clave de deduplicacion: mensaje_id, de la URL de Outlook Web.
  - PAQUETE_INSPECCION_BV/ no se toca nunca (enlace Synology publicado a BV).

Uso:
    python capturar_correo.py < payload.json
    python capturar_correo.py --json payload.json
    python capturar_correo.py --json payload.json --dry-run

Forma del payload:
{
  "mensaje_id": "AAkALgAAAAAAHYQ...",
  "fecha": "2026-05-26T09:00",
  "remitente_nombre": "Fadey Kassim",
  "remitente_email": "Fadey.Kassim@bw-water.com",
  "para": "Luis Rivera Gonzalez",
  "cc": "Shane Banks; Eduardo Yamauchi",
  "asunto": "Notification of the sale of BW Water to De Nora",
  "tipo": "notificacion",
  "adjuntos": [{"archivo": "x.pdf", "tamano": "69 KB", "destino": "adjuntos/"}],
  "enlaces": ["https://..."],
  "cuerpo": "texto integro del mensaje"
}
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude" / "skills" / "pst-extractor" / "scripts"))
try:
    from _common import sanitize  # noqa: E402
except ImportError:  # fallback autonomo si la skill no esta disponible
    import unicodedata

    def sanitize(text: str, maxlen: int = 120) -> str:
        if not text:
            return "sin_asunto"
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
        text = re.sub(r'[<>:"/\\|?*\r\n\t]+', "_", text)
        text = re.sub(r"\s+", "_", text).strip("._ ")
        return (text or "sin_asunto")[:maxlen]

RAIZ = Path(__file__).resolve().parent.parent          # CORREOS/_RECIBIDOS
PROYECTO = RAIZ.parent.parent                          # raiz del proyecto

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

DOMINIOS = {"bw-water.com": "BW WATER", "bureauveritas.com": "BUREAU VERITAS"}

TIPOS = {"submittal", "rwi", "informe-bv", "rfi", "programa",
         "notificacion", "comercial", "otro"}

# Carpeta intocable: enlace Synology publicado a Bureau Veritas el 21-Jul-2026
INTOCABLE = "PAQUETE_INSPECCION_BV"


def normalizar_id(bruto: str) -> str:
    """Devuelve el mensaje_id hasheado.

    Acepta el identificador crudo de la URL de Outlook Web (cadena base64 larga)
    o uno ya hasheado. Se guarda hasheado porque identifica igual de bien y evita
    que los filtros del navegador bloqueen la cadena base64 al devolverla.
    """
    v = (bruto or "").strip()
    if re.fullmatch(r"[0-9a-f]{16}", v):
        return v
    return hashlib.sha1(v.encode("utf-8")).hexdigest()[:16]


def contraparte_de(email: str) -> str:
    dom = (email or "").strip().lower().rsplit("@", 1)[-1]
    for d, nombre in DOMINIOS.items():
        if dom == d or dom.endswith("." + d):
            return nombre
    return ""


def ids_capturados(raiz: Path) -> dict:
    """mensaje_id -> ruta del _correo.md que ya lo tiene."""
    vistos = {}
    for md in raiz.rglob("_correo.md"):
        try:
            txt = md.read_text(encoding="utf-8")[:4000]
        except OSError:
            continue
        m = re.search(r"^mensaje_id:\s*(.+)$", txt, re.M)
        if m:
            vistos[m.group(1).strip()] = md
    return vistos


def nombre_carpeta(fecha: datetime, remitente: str, asunto: str, destino: Path) -> str:
    """Nombre canonico con cascada de fallback ante el limite de 260 caracteres."""
    dia = fecha.strftime("%Y-%m-%d")
    quien = sanitize(remitente, 28)
    for corte in (60, 40, 20):
        nombre = f"{dia}_{quien}_{sanitize(asunto, corte)}"
        if len(str(destino / nombre)) < 230:
            return nombre
    h = hashlib.md5(asunto.encode("utf-8", "ignore")).hexdigest()[:8]
    return f"{dia}_{quien}_{h}"


def yaml_escape(v: str) -> str:
    v = (v or "").replace('"', "'").replace("\n", " ").strip()
    return v


def construir_md(p: dict, contraparte: str) -> str:
    adj = p.get("adjuntos") or []
    enl = p.get("enlaces") or []
    L = ["---",
         f"mensaje_id: {p['mensaje_id']}",
         f"fecha: {p['fecha']}",
         f"remitente: {yaml_escape(p.get('remitente_nombre'))} <{p.get('remitente_email','')}>",
         f'para: "{yaml_escape(p.get("para"))}"',
         f'cc: "{yaml_escape(p.get("cc"))}"',
         f'asunto: "{yaml_escape(p.get("asunto"))}"',
         f"contraparte: {contraparte}",
         f"tipo: {p.get('tipo','otro')}"]
    if adj:
        L.append("adjuntos:")
        for a in adj:
            L.append(f'  - archivo: "{yaml_escape(a.get("archivo"))}"')
            L.append(f'    tamano: "{yaml_escape(a.get("tamano"))}"')
            L.append(f'    destino: "{yaml_escape(a.get("destino","adjuntos/"))}"')
    else:
        L.append("adjuntos: []")
    if enl:
        L.append("enlaces:")
        L += [f"  - {e}" for e in enl]
    else:
        L.append("enlaces: []")
    fecha_dia = str(p["fecha"])[:10]
    L += ["second_brain: capture", "type: correo",
          "project: salmuera-taltal", f"date: {fecha_dia}", "---", ""]

    L.append(f"# {p.get('asunto','(sin asunto)')}")
    L.append("")
    L.append(f"**De:** {p.get('remitente_nombre','')} <{p.get('remitente_email','')}>  ")
    L.append(f"**Para:** {p.get('para','')}  ")
    if p.get("cc"):
        L.append(f"**CC:** {p['cc']}  ")
    L.append(f"**Fecha:** {p['fecha']}")
    L.append("")
    if adj:
        L.append("## Adjuntos")
        L.append("")
        L.append("| Archivo | Tamaño | Destino |")
        L.append("|---|---|---|")
        for a in adj:
            L.append(f"| `{a.get('archivo','')}` | {a.get('tamano','')} | `{a.get('destino','adjuntos/')}` |")
        L.append("")
    if enl:
        L.append("## Enlaces")
        L.append("")
        L += [f"- {e}" for e in enl]
        L.append("")
    L.append("## Cuerpo")
    L.append("")
    L.append(p.get("cuerpo", "").strip())
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Captura un correo entrante a CORREOS/_RECIBIDOS/")
    ap.add_argument("--json", help="archivo con el payload; por defecto lee stdin")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, solo informa")
    args = ap.parse_args()

    crudo = Path(args.json).read_text(encoding="utf-8") if args.json else sys.stdin.read()
    p = json.loads(crudo)

    faltan = [c for c in ("mensaje_id", "fecha", "asunto", "cuerpo") if not p.get(c)]
    if faltan:
        print("ABORTA: faltan campos obligatorios: " + ", ".join(faltan), file=sys.stderr)
        return 1
    p["mensaje_id"] = normalizar_id(p["mensaje_id"])

    contraparte = contraparte_de(p.get("remitente_email", ""))
    if not contraparte:
        print(f"ABORTA: el remitente '{p.get('remitente_email')}' no es de BW Water "
              f"ni de Bureau Veritas. El alcance de esta carpeta son esos dos dominios.",
              file=sys.stderr)
        return 1

    tipo = p.get("tipo", "otro")
    if tipo not in TIPOS:
        print(f"ABORTA: tipo '{tipo}' no valido. Use uno de: {', '.join(sorted(TIPOS))}",
              file=sys.stderr)
        return 1

    for a in p.get("adjuntos") or []:
        if INTOCABLE in (a.get("destino") or ""):
            print(f"ABORTA: un adjunto apunta a {INTOCABLE}, que no se toca "
                  f"(enlace Synology publicado a Bureau Veritas).", file=sys.stderr)
            return 1

    vistos = ids_capturados(RAIZ)
    if p["mensaje_id"] in vistos:
        rel = vistos[p["mensaje_id"]].relative_to(RAIZ)
        print(f"YA CAPTURADO — sin cambios. Vive en: {rel}")
        return 0

    fecha = datetime.fromisoformat(str(p["fecha"]))
    mes = RAIZ / f"{MESES[fecha.month - 1]} {fecha.year}"
    carpeta = mes / nombre_carpeta(fecha, p.get("remitente_nombre", ""), p["asunto"], mes)

    if args.dry_run:
        print(f"[dry-run] crearia: {carpeta.relative_to(RAIZ)}")
        print(f"[dry-run] contraparte={contraparte} tipo={tipo} "
              f"adjuntos={len(p.get('adjuntos') or [])}")
        return 0

    carpeta.mkdir(parents=True, exist_ok=True)
    (carpeta / "_correo.md").write_text(construir_md(p, contraparte), encoding="utf-8")
    if any((a.get("destino") or "adjuntos/").rstrip("/") == "adjuntos"
           for a in p.get("adjuntos") or []):
        (carpeta / "adjuntos").mkdir(exist_ok=True)

    print(f"CAPTURADO: {carpeta.relative_to(RAIZ)}")
    print(f"  contraparte={contraparte} tipo={tipo} adjuntos={len(p.get('adjuntos') or [])}")
    for a in p.get("adjuntos") or []:
        d = a.get("destino", "adjuntos/")
        if d.rstrip("/") != "adjuntos":
            print(f"  PENDIENTE mover a su destino: {a.get('archivo')} -> {d}")
    print("  Regenera el indice con: python scripts/generar_registro.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
