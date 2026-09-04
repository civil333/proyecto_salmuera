# INSTRUCCIONES DE AUDIT — Plant Control Philosophy Rev B

## CONTEXTO

Auditoria multidisciplinaria del documento **Plant Control Philosophy Rev B** (P22-BT-09-009-001)
emitido por BW Water en ENTREGA 33 (22-Apr-2026), 51 paginas, 2436 lineas extraidas.

ADASA ya realizo una primera revision en Transmittal N15 (v2, 22-Apr-2026) con veredicto
Code 2 - Approved as Noted y 7 NOTEs (NOTE-13..19). Esta auditoria multi-audit busca:

1. **Validar/ampliar** los NOTEs existentes con perspectivas multi-agente
2. **Identificar findings nuevos** no cubiertos en TM N15
3. **Verificar conformidad** contractual (ET, BAE, Oferta Tecnica Rev1, Oferta Economica)
4. **Detectar regresiones** Rev A -> Rev B (aunque Rev B no tiene Consolidated Comment Sheet)
5. **Cruzar contra** documentos de control ya aprobados (IO List Rev C, Valve List Rev D,
   Instrument List Rev C, Data Transfer List Rev B, P&ID Rev C, Control System Architecture Rev D)

## NOTES YA LEVANTADOS EN TM N15 (NO DUPLICAR)

| ID | Severidad | Tema | Resumen |
|----|-----------|------|---------|
| NOTE-13 | MAJOR | SEC formula alignment | Seccion 1.4 declara 4.8-5.0 kWh/m3 por rango TDS vs Oferta Rev1 4.71 kWh/m3 +/- 5%. |
| NOTE-14 | MAJOR | Vibration setpoints | Seccion 3.2.2 describe alarm/trip sin mm/s numericos. |
| NOTE-15 | MAJOR | Antiscalant ratio source | Seccion 2.3.3 usa FIT-09-001 pero P&ID dice cartridge filter discharge. |
| NOTE-16 | MAJOR | VE-09-002 modulating | Seccion 3.2.3 sin algoritmo (PI/PID). |
| NOTE-17 | MAJOR | CIP cycle sequence | Seccion 4 sin sequence/interlock matrix. |
| NOTE-18 | MINOR | Motor RTD thresholds | Seccion 3.2.2 defiere a doc separado. |
| NOTE-19 | MINOR | Feed turbo isolation | Seccion 3.2.2 sin valvula isolation. |

## CRITERIOS DE AUDIT

### 1. Conformidad con Especificacion Tecnica (ET Modulo P22-ET-09-000-001-0)

Secciones relevantes:
- §5.1.4 Bomba de Lavado CIP — operacion CIP Pump
- §5.3 Motores Electricos — Pt-100 winding y bearing en TODOS los motores
- §5.4 Tableros fuerza y control — PLC, HMI, UPS
- §5.5 Instrumentacion — 4-20mA + HART obligatorio
  - 5.5.5 Conductimetros (toroidal salmuera concentrada)
  - 5.5.6 Vibracion
- §10 Garantias — performance

### 2. Conformidad con Oferta Tecnica Rev1 (BW Water)

- §3.2 Performance Testing
- §5 Clarifications and Deviations
- §17 Power Consumption
- §19 Guaranteed SEC: 4.71 kWh/m3 +/- 5%

### 3. Conformidad con BAE 12803 (contractual)

Performance guarantees, deadlines, scope.

### 4. Consistencia con Documentos de Control Aprobados

- IO List Rev C (141 items, TE no TIT motores, modulo 5069-IY4)
- Valve List Rev D (111 items, VE-09-002 modulating ON/OFF DN25 SDSS)
- Instrument List Rev C (39 items, VT Wilcoxon PCH420V-M12 0-127 mm/s HART 7.0)
- Data Transfer List Rev B (189 Modbus)
- P&ID Rev C
- Control System Architecture Rev D (CompactLogix 5380 + FactoryTalk + UPS 8h)

### 5. Delta Rev A -> Rev B

Rev A 06-Mar-2026 (ENTREGA 14, 48 paginas, 1653 lineas extraidas).
Rev B 22-Apr-2026 (ENTREGA 33, 51 paginas, 2436 lineas extraidas).
Rev B NO incluye Consolidated Comment Sheet — finding por si solo.

### 6. Anti-IA

Verificar que Control Philosophy no contenga frases-firma IA tipicas.

## EXTRACTOS CRITICOS DE OFERTA TECNICA REV1 — PERFORMANCE

```
Linea 491 OFERTA-TECNICA-BWWATER-Rev1.md:
SEC (Specific Energy Consumption) Test
Plant Power Panel Meter. As per project requirements, the guaranteed SEC value must remain
below 5.0 kWh/m3 at a feed TDS of 53,000 ppm.
Our guaranteed SEC (EEC) value is calculated based on the total energy consumption of all equipment

Linea 500:
The guaranteed SEC (EEC) value is 4.71 kWh/m3 +/- 5%.
This SEC value is the one to be considered for both the SEC performance guarantee and...
```

## EXTRACTOS CRITICOS DE OFERTA ECONOMICA

Ver en fuentes.md seccion correspondiente.

## FORMATO DE OUTPUT ESPERADO POR CADA AGENTE

Cada agente debe reportar:

```
## Agente: <nombre>

### Findings nuevos (no duplicar con NOTE-13..19):
- [ID SUGERIDO]: [descripcion]
  - Severidad: CRITICAL/MAJOR/MINOR/NOTE
  - Technical Basis: [ET/Oferta/BAE/control doc]
  - Seccion Control Philosophy: [§X.Y]
  - Accion requerida: [prior to IFC Rev 0] o [Rev C]

### Expansion/validacion de NOTE-13..19 existentes:
- NOTE-XX: [evidencia adicional o matiz]

### Findings desechados (por Verificador/Auditor Sombra):
- [claim X]: razon para descartar

### Veredicto del agente:
- Code sugerido: 1/2/3/4
- Nota global: X/10
- Justificacion breve
```
