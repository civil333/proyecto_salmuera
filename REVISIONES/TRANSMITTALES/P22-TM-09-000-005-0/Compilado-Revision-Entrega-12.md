---
titulo: "Compilado Revision Tecnica Entrega 12"
fecha: "23-Feb-2026"
autor: "Luis Rivera / Van Doorn"
clasificacion: "INTERNO - NO ENVIAR A BW WATER"
entrega: "ENTREGA 12"
submittal: "25007-0012"
documento: "P22-DWG-09-005-003 Rev A - Equipment Layout of RO Container"
---

# COMPILADO REVISION TECNICA - ENTREGA 12

**DOCUMENTO INTERNO ADASA - NO ENVIAR A BW WATER**

---

## 1. Datos del Documento

| Campo | Valor |
|-------|-------|
| Documento | P22-DWG-09-005-003 Rev A |
| Titulo | Equipment Layout of RO Container |
| Fecha documento | 19-Feb-2026 |
| Submittal | 25007-0012 |
| Entrega | ENTREGA 12 (20-Feb-2026) |
| Estado dibujo | ISSUED FOR APPROVAL |
| Disciplina | MECHANICAL |
| Revisado por | Luis Rivera (ADASA) con aportes Van Doorn |

---

## 2. Resumen de Hallazgos

### 2.1 Hallazgo Principal: CIP Equipment Inside Container

El plano muestra el sistema CIP completo (estanque 9,922 lb, bomba 750 lb, filtro cartucho 1,800 lb) y el estanque quimico (467 lb) **dentro** del contenedor de 40ft.

Esto contradice directamente:

1. **Oferta Tecnica Rev.1** (lineas 552-579):
   - "1 x 100% CIP / Flushing Tank package [...] **Located outside the 40 ft container**"
   - "1 x 100% CIP / Flushing Pump package [...] **Located outside the 40 ft container**"
   - "1 x 100% CIP Cartridge Filter package [...] **Located outside the 40 ft container**"
   - "1 x 100% Anti-Scalant Injection System package [...] **Located outside the 40 ft container**"

2. **Reunion Coordinacion 18-Feb-2026**: BW Water confirmo que el "CIP system [es] externo al container. Vendor enviara plano layout actualizado."

**Evaluacion Van Doorn:** La inclusion del CIP dentro del container genera multiples problemas:
- Carga termica adicional significativa (heater CIP dentro del espacio confinado)
- Peso adicional de ~12,939 lb (~5.9 toneladas) dentro del container
- Reduce espacio disponible para acceso a mantenimiento de membranas y HP pump
- Contradice la propia justificacion de la Oferta Rev1 (linea 550): "Vent fan is not needed since CIP system and chemical dosing system are located in outside the container"

Si el CIP esta dentro, la ventilacion del container requiere reevaluacion.

### 2.2 Container 40ft - POSITIVO

El plano confirma un contenedor estandar de 40ft. Largo interno util: 36'-10" (11.23m).

Esto resuelve la OBS-10 del TM N4 donde el Cable Tray Layout sugeria un container elongado >40ft. El plano de Equipment Layout confirma dimensiones dentro del limite ET 5.1.10 (max 13m x 2.5m x 2.8m).

**Conversion:** 40ft = 12.192m < 13m (CUMPLE)

### 2.3 Sistema de Unidades

Todas las dimensiones estan en sistema imperial (pies y pulgadas). El proyecto se desarrolla en Chile donde el sistema metrico es obligatorio. La ET no especifica sistema de unidades explicitamente, pero toda la documentacion ADASA y las normas chilenas usan MKS.

El revisor (markup ADASA) anoto explicitamente: "Las medidas deben estar tambien en sistema MKS".

### 2.4 Puertas No Especificadas

ET 5.1.10 (L726-732) requiere:
- Puerta peatonal: 900 mm x 2,200 mm
- Puerta de equipos: dimensiones para el equipo mas grande, apertura 110 grados, hacia exterior
- Puerta de emergencia
- Puerta lateral corrediza

El plano no muestra ninguna de estas puertas. Para un plano de Equipment Layout en estado "Issued for Approval", la ubicacion de puertas es fundamental para verificar accesos de mantenimiento y cumplimiento normativo.

### 2.5 Unidades A/C No Mostradas

ET 5.1.11 requiere n+1 unidades de A/C (minimo 2). BW Water confirmo 2 A/C (1W+1S) el 17-Feb. El layout debe mostrar la posicion de las unidades A/C para verificar:
- Espacio fisico disponible
- Acceso para mantenimiento de las unidades
- Distribucion termica adecuada

### 2.6 Piso PRFV No Indicado

ET 5.1.10 (L733): "El piso por donde caminaran los operarios debera constar de una rejilla de PRFV antideslizante."

El plano no indica material del piso. Para verificacion de cumplimiento normativo, el plano deberia notar la especificacion del piso.

### 2.7 Anclajes Sismicos Sin Detalle

ET 4.4 requiere diseno para NCh 2369, Zona 3. El plano incluye tabla de pesos (total 34,739 lb / 15,758 kg), lo cual es positivo para calculos estructurales, pero no muestra:
- Tipo de anclaje de equipos
- Puntos de fijacion al contenedor
- Referencia a memoria de calculo sismica (requerida por ET Sec 7)

### 2.8 Panel de Control Local

El LCP se muestra fuera del contenedor, consistente con la Oferta Rev1 (linea 580-581). El reviewer anoto que:
- OK con la posicion
- Pero debe estar adosado al modulo (no separado)
- Las pruebas FAT y conexion del panel son parte del alcance BW Water
- Bandejas de cables deben quedar resueltas

### 2.9 Disposicion de Equipos

La disposicion general es logica:
- Turbochargers y HP Pump en un extremo (lado feed)
- RO Pressure Vessels en la zona central (mayor espacio)
- CIP/Chemical en el otro extremo

Sin embargo, la anotacion ADASA sobre infraestructura LQ indica que las conexiones de liquidos (permeado, concentrado, alimentacion) deben alinearse a un lado del modulo para facilitar piping y conexion con la planta existente.

---

## 3. Veredicto Propuesto

**3 - TO BE REVISED**

Razon principal: El sistema CIP dentro del container contradice la Oferta Tecnica Rev1 y los acuerdos de la reunion del 18-Feb-2026. Este es un cambio de alcance no aprobado que afecta multiples aspectos del diseno (termico, estructural, acceso).

---

## 4. Observaciones Pendientes de Transmittales Anteriores (al 23-Feb-2026)

### CERRADAS (no incluir en TM N5 como pendientes)
- ~~Pt-100 motor windings~~ — CLOSED 17-Feb
- ~~Vibration transmitters~~ — CLOSED 17-Feb
- ~~Duplicate TAG FIT-09-001~~ — CLOSED 17-Feb (renombrado FIT-09-002)
- ~~A/C n+1 configuration~~ — CLOSED 17-Feb (confirmado per ET 5.1.11)
- ~~Ethernet IP PLC-VFD~~ — RATIFICADO 18-Feb (cierra OBS-12)
- ~~Container >40ft (OBS-10 TM N4)~~ — **CLOSED** por este GA (confirma 40ft)

### ABIERTAS desde TM N2 (6-Ene-2026) - 48 DIAS
1. A/C thermal calculation (OBS-03 TM N4) — documento no entregado
2. Modbus TCP Memory Map (OBS-04 TM N4) — comprometido en TM N2, no entregado

### ABIERTAS desde TM N3 (28-Ene-2026) - 26 DIAS
3. VM-09-015 manual DN100 ANSI 900# — disputa tecnica activa
4. IO List coordination signals (VFD variables, DO/DI) — parcialmente abordado

### ABIERTAS desde TM N4 (5-Feb-2026) - 18 DIAS
5. PLC 60 Hz frequency (OBS-01) — sin confirmacion 50Hz
6. HP Pump power inconsistency (OBS-08) — 4 valores sin unificar
7. UPS not in BOM (OBS-09) — sin fecha
8. LIT TAG discrepancy (OBS-13) — pendiente

**Total: 8 observaciones abiertas de TM anteriores + OBS-10 cerrada por este GA**

---

**Nota Van Doorn:** La combinacion del CIP dentro del container con la ausencia de detalles de puertas y A/C sugiere que BW Water podria estar reconfigurando internamente el layout sin consultar a ADASA. El hecho de que la reunion del 18-Feb confirmo CIP externo y 3 dias despues el plano lo muestra interno refuerza esta preocupacion. Recomiendo enfatizar en el transmittal que cualquier cambio respecto a la Oferta Rev1 requiere aprobacion formal de ADASA.
