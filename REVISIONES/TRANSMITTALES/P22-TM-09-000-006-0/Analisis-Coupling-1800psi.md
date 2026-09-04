---
titulo: "Análisis Técnico — Conformidad ADASA si ambos turbos = 1,800 psi"
tipo: analisis-interno
fecha: 2026-03-02
autor: Luis Rivera
asesor: Van Doorn
relacionado: P22-TM-09-000-006-0
uso: INTERNO — NO ENVIAR A BW WATER
---

# Análisis Técnico: ¿ADASA conforme si ambos turbos tienen coupling 1,800 psi?

**Fecha:** 02-Mar-2026 | **Preparado por:** Luis Rivera | **Uso:** Interno ADASA

---

## Contexto

TM N6 rechaza (Code 4) el datasheet Rev C de la HP Pump porque BW Water redujo el coupling del Feed Turbocharger de 2,000 psi (Rev B / línea base contractual) a 1,200 psi. El Interstage Turbocharger en Rev C usa 1,800 psi, veredicto Code 2 (Approved as Noted).

La pregunta operativa: si BW Water sube el Feed TC a 1,800 psi igualando al Interstage, ¿ADASA estaría técnicamente conforme con ambos turbos a 1,800 psi?

---

## Datos de Presión del Circuito HP

**Fuente:** Technical Proposal Rev1 — Justification of Mechanical Couplings/Joints in High Pressure (escenario: 53K TDS, 19°C, 10% margin incluido)

| Joint | Punto del circuito | Presión (bar) | Presión (psi) |
|-------|-------------------|---------------|---------------|
| 1 | Descarga HP Pump | 67.50 bar | 979 psi |
| 2 | Feed TC outlet → 1ª etapa RO | **69.53 bar** | **1,009 psi** |
| 3 | Interstage TC inlet (1ª etapa concentrate) | 83.90 bar | 1,217 psi |
| 4 | Interstage TC outlet → 2ª etapa RO | **83.90 bar** | **1,217 psi** |
| 5 | 2ª etapa concentrate post-turbo | 82.40 bar | 1,195 psi |

**Nota relevante:** 83.9 bar ya incorpora el 10% safety margin del diseño. La presión real de operación en condiciones nominales es menor.

---

## Análisis de Conformidad a 1,800 psi

1,800 psi = 124.1 bar

### Feed Turbocharger — máxima presión operación: 69.53 bar (1,009 psi)

| Métrica | Valor |
|---------|-------|
| Rating propuesto | 1,800 psi (124.1 bar) |
| Presión máxima operación | 69.53 bar (1,009 psi) |
| Safety margin efectivo | **1.79x** (124.1 / 69.53) |
| Estándar mínimo para brine concentrada (ASME) | 1.5x |
| Resultado | ✅ **CONFORME** |

Con 1,800 psi el Feed TC tiene margen holgado. No hay argumento técnico de presión para rechazarlo.

### Interstage Turbocharger — máxima presión operación: 83.90 bar (1,217 psi)

| Métrica | Valor |
|---------|-------|
| Rating propuesto | 1,800 psi (124.1 bar) |
| Presión máxima operación | 83.90 bar (1,217 psi) |
| Safety margin efectivo | **1.479x** (124.1 / 83.9) |
| Estándar mínimo | 1.5x |
| Resultado | ⚠️ **MARGINAL** — ya aceptado por ADASA en Rev C (Code 2) |

El margen 1.479x está levemente bajo el estándar teórico 1.5x. ADASA aceptó esto con nota porque el 83.9 bar incluye margen de diseño del 10%, de modo que la presión real de operación tiene buffer adicional.

---

## Veredicto

### ¿Estaría ADASA técnicamente conforme si ambos turbos son 1,800 psi?

**Sí, con nota condicionada — Code 2, no Code 1.**

| Turbocharger | Rev B (línea base) | Rev C actual | Hipótesis Rev D (1,800 psi) | Código ADASA |
|---|---|---|---|---|
| Feed TC | 2,000 psi ✅ | 1,200 psi ❌ | 1,800 psi ⚠️ | Code 2 (de Code 4) |
| Interstage TC | 2,000 psi ✅ | 1,800 psi ⚠️ | 1,800 psi ⚠️ | Code 2 (sin cambio) |
| **Documento global** | Code 1 | **Code 4** | **Code 2** | Mejora sustancial |

La condición (nota) que ADASA mantendría en un Rev D a 1,800 psi:
- Interstage TC: margen 1.479x levemente bajo el estándar 1.5x; aceptado porque el 83.9 bar de diseño incorpora 10% de buffer
- Solicitar datasheet del coupling de 1,800 psi con modelo específico del fabricante
- Confirmar que el producto es clasificado para HPB service (no RO estándar)

**No se puede otorgar Code 1** porque el margen del Interstage es marginalmente bajo y la documentación del coupling de 1,800 psi está pendiente de recibir.

---

## Matices y Riesgos

### 1. ¿Existe un coupling Piedmont de 1,800 psi?

Los documentos disponibles identifican dos modelos Piedmont con certeza:

- **Style H:** 2,000 psi — diseñado explícitamente para HPB Energy Recovery turbochargers (lo especificado en Rev B)
- **Style D:** 1,200 psi — producto para RO estándar (lo propuesto en Feed TC Rev C)

No hay evidencia documental de un Piedmont a 1,800 psi. Si el Interstage TC en Rev C ya usa 1,800 psi, BW Water emplea un modelo cuyo datasheet no ha sido entregado a ADASA. La nota del Code 2 debe incluir esta solicitud explícita.

### 2. Argumento de clase de producto (aplica incluso a 1,800 psi)

El problema central no es solo el rating numérico. Si el coupling de 1,800 psi no es el Piedmont Style H clasificado para HPB turbochargers, aplica el argumento de sustitución de clase inferior: BW Water reemplazó un componente diseñado para este servicio específico por uno cuya certificación de servicio no está documentada. La nota debe registrar esto.

### 3. Ground 3 (breach of formal commitment) — Aplicabilidad reducida a 1,800 psi

Con ambos turbos a 1,800 psi, el argumento de incumplimiento formal pierde peso considerable. ADASA ya aceptó el Interstage a 1,800 psi. Mantener el rechazo del Feed TC si también sube a 1,800 psi sería inconsistente y difícil de sostener técnicamente. El argumento de desviación de línea base contractual (2,000 psi) permanece válido como nota, no como causa de rechazo.

### 4. Posición preferida de ADASA

La aceptación a 1,800 psi no significa que ADASA renuncia a la preferencia por 2,000 psi (Style H). La nota debe documentar: *"Acceptable with pending coupling documentation; ADASA's preferred solution remains return to 2,000 psi (Piedmont Style H) which constituted the contractual baseline."*

---

## Conclusión Operativa

Si BW Water presenta datasheet Rev D con ambos turbos a 1,800 psi:

1. **ADASA cambia veredicto de Code 4 → Code 2** (no Code 1 — la nota es obligatoria)
2. La nota debe documentar tres puntos:
   - Interstage TC: margen 1.479x marginalmente bajo 1.5x estándar; aceptado por el 10% buffer en presión de diseño
   - Solicitud del datasheet del coupling de 1,800 psi con modelo específico y certificación de servicio HPB
   - Preferencia de ADASA por retorno a 2,000 psi (Piedmont Style H) como línea base contractual
3. Si BW Water no entrega el datasheet del coupling con la Rev D, ADASA puede condicionar la aceptación a ese documento

---

## Fuentes

- Technical Proposal Rev1 — Justification of Mechanical Couplings/Joints in High Pressure
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-006-0/Compilado-TM6.md` — análisis Van Doorn, §4 y §5
- `REVISIONES/TRANSMITTALES/P22-TM-09-000-006-0/P22-TM-09-000-006-0_TRANSMITTAL.md`
- `BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md` — §5.2.2 (criterios de presión y materiales)
- `OFERTA TECNICA/md/OFERTA-TECNICA-BWWATER-Rev1.md` — §13
