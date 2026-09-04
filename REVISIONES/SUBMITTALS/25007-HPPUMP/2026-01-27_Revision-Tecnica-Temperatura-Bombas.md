# Revision Tecnica Cruzada: Medicion de Temperatura de Bombas

**Fecha:** 27 de enero de 2026
**Proyecto:** P22 - Modulo RO Segunda Etapa para Salmuera - PD Taltal
**Revision por:** ADASA
**Documento de referencia:** P22-ET-09-000-001-0 (Especificacion Tecnica)

---

## 1. OBJETIVO

Documentar las discrepancias entre los requisitos de la ET (P22-ET-09-000-001-0), los compromisos de la Oferta Tecnica Rev.1, y lo entregado por BW Water respecto a la medicion de temperatura de bombas.

---

## 2. REQUISITOS DE LA ESPECIFICACION TECNICA (P22-ET-09-000-001-0)

### 2.1 Requisito 1: RTDs en Bomba de Alta Presion

| Campo | Valor |
|-------|-------|
| **Seccion** | 5.1.1 Bomba de Alta Presion |
| **Pagina** | 10 |
| **Linea** | 502 |
| **Texto exacto** | "Instrumentacion RTDs a 3 hilos para temperatura de rodamientos" |
| **Caracter** | OBLIGATORIO (especificado en tabla de datos del equipo) |

### 2.2 Requisito 2: RTDs en Bomba CIP

| Campo | Valor |
|-------|-------|
| **Seccion** | 5.1.4 Bomba de lavado CIP |
| **Pagina** | 12 |
| **Linea** | 581 |
| **Texto exacto** | "Instrumentacion RTDs a 3 hilos para rodamientos" |
| **Caracter** | OBLIGATORIO (especificado en tabla de datos del equipo) |

### 2.3 Requisito 3: Pt-100 en TODOS los Motores (Devanados Y Rodamientos)

| Campo | Valor |
|-------|-------|
| **Seccion** | 5.3 Especificacion de motores electricos |
| **Pagina** | 18 |
| **Lineas** | 1032-1033 |
| **Texto exacto** | "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos." |
| **Caracter** | OBLIGATORIO - Aplica a TODOS los motores del modulo |
| **Alcance** | Motor Bomba HP (86 kW), Motor Bomba CIP (15 kW), otros motores con VFD |

---

## 3. EVIDENCIA EN DOCUMENTOS BW WATER

### 3.1 Datasheet Bomba HP (P22-ET-09-009-002-B)

**Seccion MOTOR, linea 155:**
> "Inclusion 3-wire RTDs for bearing temperature"

**Observacion:** El datasheet especifica RTDs 3 hilos para temperatura de rodamientos del conjunto bomba-motor (FEDCO), pero:
- **NO especifica** si los RTDs son tipo Pt-100
- **NO incluye** sensores de temperatura para devanados del motor
- El motor es ABB de 125 HP (87 kW) con VFD

### 3.2 IO List (P22-LI-09-008-001-A)

| TAG | Descripcion | Tipo Senal | P&ID |
|-----|-------------|------------|------|
| TE09-001-XB001 | RO HP PUMP TEMPERATURE SWITCH HIGH | DI - Dry Contact (N.O) 24VDC | P9 |
| TE09-002-XB001 | CIP PUMP TEMPERATURE SWITCH HIGH | DI - Dry Contact (N.O) 24VDC | P10 |

**Problema identificado:**
- Ambos TE son **entradas digitales (DI)**, NO analogicas (AI)
- Son **switches de temperatura** (TSH), NO transmisores
- Solo proveen alarma binaria ON/OFF, sin monitoreo continuo
- La ET Seccion 5.5 requiere instrumentacion con "protocolo 4-20mA + HART"

### 3.3 Instrument List (P22-LI-09-008-003-A)

| TAG | Descripcion | Ubicacion |
|-----|-------------|-----------|
| TIT-09-001 | CIP Tank Temperature Transmitter | CIP Tank Side |

**Problema identificado:**
- El **unico transmisor de temperatura (TIT)** es para el Tanque CIP
- **NO hay TIT** para Bomba HP ni Bomba CIP
- Los TE de bombas NO aparecen en la Instrument List (solo en IO List como switches)

### 3.4 Bomba CIP - Sin Datasheet Especifico

- No se ha identificado datasheet de Bomba CIP (BH-09-002)
- No hay especificacion de RTDs para rodamientos
- No hay especificacion de Pt-100 para motor

---

## 4. MATRIZ DE CUMPLIMIENTO

### 4.1 Bomba de Alta Presion (BH-09-001) - Motor 86 kW

| Requisito ET | Seccion/Linea | Texto ET | Entregado BW Water | Documento BW | Estado |
|--------------|---------------|----------|-------------------|--------------|--------|
| RTDs 3 hilos rodamientos bomba | 5.1.1 / L502 | "RTDs a 3 hilos para temperatura de rodamientos" | SI - "3-wire RTDs for bearing temperature" | P22-ET-09-009-002-B (L155) | **CUMPLE** |
| RTDs tipo Pt-100 | 5.3 / L1032-1033 | "sensores de temperatura tipo Pt-100" | NO especificado si RTDs son Pt-100 | P22-ET-09-009-002-B | **VERIFICAR** |
| Pt-100 devanados motor | 5.3 / L1032-1033 | "Pt-100 para devanados y rodamientos" | NO especificado | P22-ET-09-009-002-B | **INCUMPLE** |
| Senal 4-20mA + HART | 5.5 (general) | Protocolo instrumentacion | Switch digital DI (TE09-001-XB001) | P22-LI-09-008-001-A (L111) | **INCUMPLE** |

### 4.2 Bomba CIP (BH-09-002) - Motor 15 kW

| Requisito ET | Seccion/Linea | Texto ET | Entregado BW Water | Documento BW | Estado |
|--------------|---------------|----------|-------------------|--------------|--------|
| RTDs 3 hilos rodamientos | 5.1.4 / L581 | "RTDs a 3 hilos para rodamientos" | NO especificado | Sin datasheet | **INCUMPLE** |
| Pt-100 devanados motor | 5.3 / L1032-1033 | "Pt-100 para devanados y rodamientos" | NO especificado | Sin datasheet | **INCUMPLE** |
| Pt-100 rodamientos motor | 5.3 / L1032-1033 | "Pt-100 para devanados y rodamientos" | NO especificado | Sin datasheet | **INCUMPLE** |
| Senal 4-20mA + HART | 5.5 (general) | Protocolo instrumentacion | Switch digital DI (TE09-002-XB001) | P22-LI-09-008-001-A (L272) | **INCUMPLE** |

---

## 5. OBSERVACIONES

### OBS-TEMP-01: Ausencia de Pt-100 en devanados de motor Bomba HP

| Campo | Valor |
|-------|-------|
| **Documento** | P22-ET-09-009-002-B (Datasheet RO HP Pump) |
| **Pagina/Seccion** | Pagina 2, Seccion MOTOR |
| **Categoria** | Tecnico |
| **Severidad** | **CRITICO** |

**Descripcion:**
El datasheet FEDCO especifica RTDs 3 hilos para temperatura de rodamientos pero NO incluye sensores de temperatura (Pt-100) para los devanados del motor ABB de 125 HP (87 kW).

**Requisito:**
ET Seccion 5.3, Pagina 18, Lineas 1032-1033: "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos."

**Impacto:**
- Proteccion termica incompleta del motor principal de 86 kW con VFD
- El motor opera a velocidad variable, lo cual genera calentamiento adicional en devanados
- Riesgo de falla prematura por sobrecalentamiento no detectado

**Accion Requerida:**
BW Water debera confirmar que el motor ABB incluye Pt-100 en devanados o actualizar la especificacion para incluirlos.

---

### OBS-TEMP-02: Bomba CIP sin RTDs en rodamientos

| Campo | Valor |
|-------|-------|
| **Documento** | Sin datasheet especifico de Bomba CIP |
| **Pagina/Seccion** | N/A |
| **Categoria** | Tecnico |
| **Severidad** | **CRITICO** |

**Descripcion:**
No se ha entregado datasheet de la Bomba CIP (BH-09-002). La Instrument List P22-LI-09-008-003-A no incluye sensores de temperatura para esta bomba. Solo existe un switch de temperatura (TE09-002-XB001) en la IO List.

**Requisito:**
ET Seccion 5.1.4, Pagina 12, Linea 581: "Instrumentacion RTDs a 3 hilos para rodamientos"

**Impacto:**
- Motor de 15 kW sin proteccion termica de rodamientos
- No es posible monitorear condicion de la bomba CIP

**Accion Requerida:**
BW Water debera entregar datasheet de Bomba CIP incluyendo RTDs 3 hilos para rodamientos.

---

### OBS-TEMP-03: Ausencia de Pt-100 en devanados de motor Bomba CIP

| Campo | Valor |
|-------|-------|
| **Documento** | Sin datasheet especifico de Bomba CIP |
| **Pagina/Seccion** | N/A |
| **Categoria** | Tecnico |
| **Severidad** | **CRITICO** |

**Descripcion:**
No hay especificacion de Pt-100 para devanados del motor de la Bomba CIP de 15 kW.

**Requisito:**
ET Seccion 5.3, Pagina 18, Lineas 1032-1033: "Los motores deberan contar con sensores de temperatura tipo Pt-100 para devanados y rodamientos."

**Impacto:**
- Proteccion termica incompleta del motor de 15 kW
- Aplica a todos los motores del modulo segun la ET

**Accion Requerida:**
BW Water debera especificar Pt-100 en devanados del motor de Bomba CIP.

---

### OBS-TEMP-04: Switches digitales en lugar de transmisores 4-20mA+HART

| Campo | Valor |
|-------|-------|
| **Documento** | P22-LI-09-008-001-A (IO List) |
| **Pagina/Seccion** | Paginas 2-3 |
| **Categoria** | Tecnico |
| **Severidad** | **MAYOR** |

**Descripcion:**
Los sensores de temperatura de bombas (TE09-001-XB001, TE09-002-XB001) estan configurados como entradas digitales (DI) con contacto seco N.O. Esto indica que son switches de temperatura (TSH) que solo proveen alarma ON/OFF.

**Requisito:**
La ET Seccion 5.5 establece protocolo de comunicacion 4-20mA + HART para instrumentacion. Los switches digitales no cumplen este requisito.

**Impacto:**
- No permite monitoreo continuo de temperatura
- Solo se detecta cuando se supera el umbral de alarma
- No es posible tendencia historica ni analisis predictivo
- Inconsistente con el resto de la instrumentacion (transmisores con HART)

**Accion Requerida:**
BW Water debera evaluar la inclusion de transmisores de temperatura (TIT) con senal 4-20mA+HART para bombas HP y CIP, o justificar tecnicamente el uso de switches si los RTDs del equipo no permiten conexion a transmisores externos.

---

### OBS-TEMP-05: Instrument List sin sensores de temperatura para bombas

| Campo | Valor |
|-------|-------|
| **Documento** | P22-LI-09-008-003-A (Instrument List) |
| **Pagina/Seccion** | Pagina 1 |
| **Categoria** | Documentacion |
| **Severidad** | **MENOR** |

**Descripcion:**
La Instrument List solo incluye TIT-09-001 (CIP Tank Temperature Transmitter). Los sensores de temperatura de bombas (TE09-001, TE09-002) no aparecen en este listado, aunque si estan en la IO List como switches.

**Impacto:**
- Documentacion incompleta de instrumentacion de temperatura
- Inconsistencia entre IO List e Instrument List

**Accion Requerida:**
BW Water debera actualizar la Instrument List para incluir todos los sensores de temperatura, o aclarar si los switches de temperatura estan fuera del alcance de este documento.

---

## 6. ACCIONES REQUERIDAS A BW WATER

| # | Accion | Documento a Actualizar | Requisito ET | Prioridad |
|---|--------|------------------------|--------------|-----------|
| 1 | Confirmar/incluir Pt-100 en devanados del motor de Bomba HP (87 kW ABB) | P22-ET-09-009-002 | 5.3 L1032-1033 | **CRITICO** |
| 2 | Entregar datasheet de Bomba CIP con RTDs 3 hilos para rodamientos | Nuevo: Datasheet Bomba CIP | 5.1.4 L581 | **CRITICO** |
| 3 | Confirmar/incluir Pt-100 en devanados del motor de Bomba CIP (15 kW) | Datasheet Bomba CIP | 5.3 L1032-1033 | **CRITICO** |
| 4 | Confirmar/incluir Pt-100 en rodamientos del motor de Bomba CIP | Datasheet Bomba CIP | 5.3 L1032-1033 | **CRITICO** |
| 5 | Evaluar transmisores 4-20mA+HART (TIT) para temperatura de bombas, o justificar tecnicamente el uso de switches | IO List / Instrument List | 5.5 | **ALTO** |
| 6 | Actualizar Instrument List con sensores de temperatura de bombas | P22-LI-09-008-003 | Documentacion | MEDIO |

---

## 7. NOTAS TECNICAS

### 7.1 Diferencia RTD vs Pt-100

- **RTD (Resistance Temperature Detector):** Termino generico para sensores de temperatura por resistencia
- **Pt-100:** Tipo especifico de RTD con resistencia de 100 ohms a 0°C, de platino
- **Requisito ET:** Especifica "tipo Pt-100", lo cual es mas exigente que RTD generico
- **Verificacion:** Si BW Water provee RTDs, debe confirmar que son Pt-100 (resistencia 100 ohms @ 0°C)

### 7.2 Devanados vs Rodamientos

La ET tiene dos niveles de requisitos:
1. **Seccion 5.1.1/5.1.4:** Solo menciona rodamientos (requisito minimo para la bomba)
2. **Seccion 5.3:** Requiere AMBOS (devanados Y rodamientos) para todos los motores

**Aplicacion:** Aplica el requisito mas exigente (5.3). Los motores deben tener Pt-100 en devanados Y rodamientos.

### 7.3 Justificacion de Severidad CRITICO

Los sensores de temperatura en motores son elementos de proteccion criticos:
- Detectan sobrecalentamiento antes de falla catastrofica
- Motor HP de 87 kW con VFD: operacion variable aumenta estres termico
- Ambiente marino corrosivo: fallas mecanicas pueden generar friccion y calentamiento
- Costo de reemplazo de motor >> costo de sensores Pt-100

### 7.4 Equipos sin requisito de temperatura

- **Bomba Dosificadora de Anti-incrustante:** Motor de 24W, no requiere sensores de temperatura por su baja potencia

---

## 8. ARCHIVOS FUENTE CONSULTADOS

| Documento | Ubicacion | Contenido Relevante |
|-----------|-----------|---------------------|
| P22-ET-09-000-001-0 | BASES TECNICAS/md/P22-ET-09-000-001-0-ET-MODULO.md | Secciones 5.1.1 (L502), 5.1.4 (L581), 5.3 (L1032-1033) |
| P22-ET-09-009-002-B | ENTREGAS_BWWATER/ENTREGA 7/md/ | Datasheet RO HP Pump - Motor section L155 |
| P22-LI-09-008-001-A | ENTREGAS_BWWATER/ENTREGA 8/md/ | IO List - TE09-001 (L111), TE09-002 (L272) |
| P22-LI-09-008-003-A | ENTREGAS_BWWATER/ENTREGA 8/md/ | Instrument List - TIT-09-001 (L143-150) |

---

## 9. CONCLUSION

Se identificaron **5 observaciones** relacionadas con la medicion de temperatura de bombas:
- **3 CRITICOS:** Falta de Pt-100 en devanados de ambos motores, falta de RTDs en Bomba CIP
- **1 MAYOR:** Uso de switches digitales en lugar de transmisores
- **1 MENOR:** Documentacion incompleta

**Veredicto propuesto para documentos afectados:**
- P22-ET-09-009-002-B (Datasheet HP Pump): **3 - To be revised**
- P22-LI-09-008-001-A (IO List): **2 - Approved as noted** (con comentarios sobre TE switches)
- P22-LI-09-008-003-A (Instrument List): **2 - Approved as noted** (con comentarios sobre documentacion)

---

*Documento generado: 27 de enero de 2026*
*Revisor: ADASA*
