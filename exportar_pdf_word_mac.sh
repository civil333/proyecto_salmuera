#!/bin/zsh
# Export docx -> PDF con Microsoft Word para Mac (TOC/campos reales), 10-jul-2026.
# Equivalente macOS de exportar_pdf_word.ps1 (Windows, Word COM). Uso:
#   ./exportar_pdf_word_mac.sh <entrada.docx> [salida.pdf]
# Actualiza todos los campos y tablas de contenido antes de exportar.
# Gotcha: Word debe tener permiso de Automation para el terminal (System Settings
# > Privacy & Security > Automation); la primera corrida puede pedir confirmación.

set -euo pipefail

DOCX="$1"
PDF="${2:-${DOCX%.docx}.pdf}"

if [[ ! -f "$DOCX" ]]; then
  echo "ERROR: no existe $DOCX" >&2
  exit 1
fi

# Rutas absolutas (Word resuelve mejor con absolutas)
DOCX="$(cd "$(dirname "$DOCX")" && pwd)/$(basename "$DOCX")"
case "$PDF" in
  /*) : ;;
  *) PDF="$(pwd)/$PDF" ;;
esac

# Notas de sintaxis (medidas 10-jul-2026): (1) Word para Mac rechaza `save as` sobre
# una variable (`set d to active document; save as d ...` da -1708); funciona SOLO la
# forma directa `save as active document ...`, con un delay tras open. (2) La forma
# `open POSIX file ...` puede quedar MUDA (Word acepta el evento y no abre nada, docs=0,
# típico tras un cuelgue o con la galería de inicio); la forma `open file name "<ruta
# posix como string>"` usa otro code path y abre siempre — usarla SIEMPRE.
#
# (3) ESCRITURA EN CloudStorage (medido 14-ago-2026, Word 16.112): el sandbox de Word
# NO puede escribir bajo ~/Library/CloudStorage/ (Synology Drive, OneDrive, iCloud).
# `save as` hacia esa ruta devuelve -1708 SIEMPRE, venga el documento de donde venga:
# se comprobó abriendo el mismo .docx desde /private/tmp y desde CloudStorage, y el
# fallo depende solo del destino. LEER de CloudStorage sí funciona.
# El directorio de paso va en /private/tmp y NO en $TMPDIR: el $TMPDIR del usuario
# cuelga de /var/folders/... y el sandbox de Word tampoco lo alcanza (Word acepta el
# `open`, no abre nada y el script muere con -2700). /private/tmp está comprobado.
#
# (4) EL DIRECTORIO DE PASO VA DENTRO DEL CONTENEDOR DE WORD (medido 18-ago-2026).
# La versión anterior creaba el paso con `mktemp -d /private/tmp/word_pdf_export.XXXXXX`,
# es decir una RUTA NUEVA EN CADA CORRIDA. Word es una app sandboxed: ante cualquier ruta
# que el usuario no le haya autorizado explícitamente levanta el diálogo Powerbox
# "Conceder acceso al archivo ... Selecciona el elemento para conceder acceso". Como el
# nombre cambiaba cada vez, la autorización nunca servía para la corrida siguiente y el
# diálogo aparecía SIEMPRE. Ese era el permiso que el usuario veía, no el de
# automatización ni el de volúmenes de red.
# La solución no es una carpeta fija en /private/tmp (seguiría siendo ruta ajena al
# sandbox) sino el propio contenedor de Word, al que Word accede sin pedir nada:
#   ~/Library/Containers/com.microsoft.Word/Data/
# El shell escribe ahí sin problema y mueve el PDF al proyecto al terminar.
#
# Sigue valiendo lo de (3): el destino final NO puede estar en CloudStorage, y por eso el
# PDF lo mueve el shell y no Word.
#
# Para que Word abra y escriba directo en la carpeta del proyecto (requiere concederle
# acceso a volúmenes de red o Full Disk Access una sola vez):
#   WORD_DIRECTO=1 ./exportar_pdf_word_mac.sh <entrada.docx>
case "${WORD_DIRECTO:-0}" in
  1) USA_ESCALA=0 ;;
  *) USA_ESCALA=1 ;;
esac

if (( USA_ESCALA )); then
  # Ruta ESTABLE dentro del contenedor de Word: sin diálogo de Powerbox.
  STAGE="$HOME/Library/Containers/com.microsoft.Word/Data/pdf_export"
  if [[ ! -d "$(dirname "$STAGE")" ]]; then
    echo "ERROR: no existe el contenedor de Word; usar WORD_DIRECTO=1" >&2
    exit 4
  fi
  mkdir -p "$STAGE"
  trap 'rm -f "$WORK_DOCX" "$WORK_PDF"' EXIT
  WORK_DOCX="$STAGE/$(basename "$DOCX")"
  WORK_PDF="$STAGE/$(basename "$PDF")"
  cp "$DOCX" "$WORK_DOCX"
  echo "[info] Word trabaja en $STAGE; el shell mueve el PDF al proyecto"
else
  WORK_DOCX="$DOCX"
  WORK_PDF="$PDF"
fi

osascript <<EOF
tell application "Microsoft Word"
    open file name "$WORK_DOCX"
    -- Esperar la apertura en vez de fijar un retardo: en la primera corrida del día
    -- Word arranca frío y tres segundos no siempre alcanzan.
    set intentos to 0
    repeat until (count of documents) > 0 or intentos > 20
        delay 1
        set intentos to intentos + 1
    end repeat
    if (count of documents) is 0 then error "Word no abrió el documento"
    delay 1
    try
        repeat with t in (tables of contents of active document)
            update t
        end repeat
    end try
    try
        set fieldCount to count of fields of active document
        repeat with i from 1 to fieldCount
            update field (field i of active document)
        end repeat
    end try
    save as active document file name "$WORK_PDF" file format format PDF
    close active document saving no
end tell
EOF

if [[ ! -f "$WORK_PDF" ]]; then
  echo "ERROR: Word no escribió el PDF en $WORK_PDF" >&2
  exit 2
fi
if (( USA_ESCALA )); then
  mv -f "$WORK_PDF" "$PDF"
fi

# Word deja su archivo de bloqueo ~$nombre.docx si la corrida anterior murió a medias.
# Con el documento ya cerrado, se puede retirar sin riesgo; si queda, la próxima
# apertura entra en modo solo lectura y el ciclo se rompe con -1712.
LOCK="$(dirname "$DOCX")/~\$$(basename "$DOCX" | cut -c3-)"
if [[ -f "$LOCK" ]]; then
  rm -f "$LOCK"
fi

# Verificación: el PDF debe existir y pesar algo razonable
if [[ ! -f "$PDF" ]]; then
  echo "ERROR: Word no escribió $PDF" >&2
  exit 2
fi
SZ=$(stat -f "%z" "$PDF")
if (( SZ < 50000 )); then
  echo "ADVERTENCIA: $PDF pesa solo $SZ bytes — revisar" >&2
  exit 3
fi
echo "OK PDF: $PDF ($SZ bytes)"
