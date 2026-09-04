# Revision Tecnica - Entrega 3 BW Water

**Submittal:** 25007-0003
**Fecha Emision:** 16-Dic-2025
**Fecha Revision:** 12-Ene-2026
**Revisor:** ADASA
**Version:** 3.2 (incluye analisis critico de inconsistencias Van Doorn vs ADASA)

---

## 1. Resumen de la Entrega

| Campo | Valor |
|-------|-------|
| Submittal No. | 25007-0003 |
| Fecha Emision | 16-Dic-2025 |
| Documentos | 1 |
| Tipo | DWG (Plano) |
| Submittal For | FA (For Approval) |

---

## 2. Documento Recibido

| # | Codigo | Rev | Titulo | Tipo | Paginas |
|---|--------|-----|--------|------|---------|
| 1 | P22-DWG-09-009-002 | A | Piping & Instrumentation Diagram (P&ID) | DWG | 12 |

---

## 3. Verificacion vs Ingenieria Basica ADASA

### 3.1 Verificacion de TIE-INs (Puntos de Conexion)

El P&ID del modulo BW Water (area 09) debe conectarse con los sistemas ADASA (area 06) en 5 puntos definidos en la Ingenieria Basica.

| TIE-IN | Fluido | Linea ADASA | DN | P&ID ADASA | Conexion BW Water | Estado |
|--------|--------|-------------|----|-----------|--------------------|--------|
| TIE-IN 1 | Salmuera entrada | SA-HDPE-DN110-PN10-005 | 110 | P22-DWG-06-009-002 | DA-SDSS-DN100-09-001 (SWRO Brine Feed) | **OK** |
| TIE-IN 2 | Permeado salida | PE-HDPE-DN90-PN10-001 | 90 | P22-DWG-06-009-003 | PE-PVC-DN80-09-012/013 (Common Permeate) | **OK** |
| TIE-IN 3 | Rechazo salmuera | SA-HDPE-DN90-PN10-002 | 90 | P22-DWG-06-009-003 | DA-SDSS-DN100-09-003 (RO Reject) | **OK** |
| TIE-IN 4 | Drenajes CIP | SA-HDPE-DN90-PN10-003 | 90 | P22-DWG-06-009-005 | DA-SDSS-DN65-09-008/009 (CIP Drains) | **OK** |
| TIE-IN 5 | Dispersante | DI-PVC interno | - | P22-DWG-06-009-005 | AS-PVC-DN25-09-031 (Antiscalant) | **VERIFICAR** |

**Observacion TIE-IN 5:** El estanque de dispersante TK-06-003 aparece en P&ID ADASA (P22-DWG-06-009-005) pero segun Lista de Equipos (P22-LI-06-005-001) es suministro BW Water. Confirmar responsabilidad.

### 3.2 Verificacion de Equipos vs Lista de Equipos ADASA

**Referencia:** P22-LI-06-005-001 (Lista de Equipos Electromecanicos)

| TAG ADASA | TAG BW Water | Descripcion | Capacidad ADASA | Capacidad BW Water | Estado |
|-----------|--------------|-------------|-----------------|--------------------| ------|
| TK-06-001 | - | Estanque Salmuera | 10.000 L | (Externo al modulo) | **N/A** |
| TK-06-002 | TK-09-001 | Estanque CIP | 5.100 L | 5.1 m3 | **COINCIDE** |
| TK-06-003 | TK-09-002 | Estanque Dispersante | - | 0.25 m3 | **OK** |
| BH-06-001 | - | Bomba Alimentacion | 13.4 l/s, 40 mca | (Externo al modulo) | **N/A** |
| BH-06-002 | BH-09-001 | Bomba Alta Presion | 13.4 l/s, 877 mca, 225 kW | VSD (sin datos) | **FALTA DETALLE** |
| BH-06-003 | SIP-09-001 | Turbo 1ra Etapa | - | 49 m3/h @ 63.21 barg | **OK** |
| BH-06-004 | SIP-09-002 | Turbo 2da Etapa | - | 35.11 m3/h @ 77.1 barg | **OK** |
| BH-06-005 | BH-09-002 | Bomba CIP | 15.8 l/s, 41.8 mca, 11 kW | 57.2 m3/h @ 4.1 barg | **COINCIDE** |
| FC-06-001 | FIL-09-001 | Filtro RO Cartucho | 49 m3/h | 49 m3/h, FRP | **COINCIDE** |
| FC-06-002 | FIL-09-002 | Filtro CIP Cartucho | 57.2 m3/h | 57.2 m3/h, FRP/PP | **COINCIDE** |
| BOI-06-001 | BOI-09-001 | Rack OI 1ra Etapa | 6 tubos x 7 elem | 6 PVs | **COINCIDE** |
| BOI-06-002 | BOI-09-002 | Rack OI 2da Etapa | 4 tubos x 7 elem | 4 PVs | **COINCIDE** |

**Observaciones Equipos:**
1. BH-09-001 (HP Pump): P&ID muestra VSD pero no detalla caudal/TDH. Debe verificarse vs datasheet P22-ITEM-09-009-002.
2. REL-09-001 (CIP Heater): 20 kW - No aparece en Lista Equipos ADASA pero SI en P&ID BW Water. OK.

### 3.3 Verificacion de Materiales vs ET Canerias ADASA

**Referencia:** P22-ET-06-006-001 (Especificacion Tecnica de Canerias y Valvulas)

| Componente | Especificacion ADASA | Especificacion BW Water | Estado |
|------------|---------------------|------------------------|--------|
| Lineas externas (ADASA) | HDPE PE100 SDR17 PN10 | N/A | **OK** |
| Lineas internas AP (BW) | Super Duplex PREN>40 | SSD (Super Duplex 2507) | **CUMPLE** |
| Lineas internas BP (BW) | PVC SCH80 | PVC | **CUMPLE** |
| Turbochargers | Super Duplex PREN>40 | SDSS 2507 (PREN~42) | **CUMPLE** |
| Bomba CIP cuerpo | SS316 | SS316 | **CUMPLE** |
| Tanque CIP | HDPE | HDPE | **CUMPLE** |
| Filtros | FRP | FRP | **CUMPLE** |
| Valvulas check | Super Duplex 2507 | No especificado en P&ID | **FALTA** |
| Empaquetaduras | NBR/SBR ASME B16.21 | No indicado | **FALTA** |

### 3.4 Verificacion de Instrumentos vs Lista Instrumentos ADASA

**Referencia:** P22-LI-06-008-001 (Lista de Instrumentos)

| Instrumento ADASA | TAG | Suministro | Mostrado en P&ID BW | Estado |
|-------------------|-----|-----------|---------------------|--------|
| Caudalimetro Alimentacion | FIT-06-001 | ADASA | No (externo) | **OK** |
| Transmisor Presion | PIT-06-001 | ADASA | No (externo) | **OK** |
| Analizador ORP | ORPIT-06-001 | **BW Water** | ORP-IT-09-001 | **CUMPLE** |
| Conductivimetro Permeado | CONDIT-06-001 | **BW Water** | AIT-09-002/003 | **CUMPLE** |
| Switches Nivel TK | LSH/LSL-06-001 | ADASA | No (externo) | **OK** |
| Transmisor Nivel TK | LIT-06-001 | ADASA | No (externo) | **OK** |

**Instrumentos adicionales BW Water (mostrados en P&ID):**
- 9+ Transmisores de presion (PIT-09-001 a 009)
- 4+ Caudalimetros (FIT-09-001, 003, 004, 005)
- 2 Transmisores temperatura (TIT-09-001, 002)
- 2 Indicadores nivel (LI-09-001, 002)
- 2 Switches nivel (LS-09-001, 002)
- 2+ Analizadores conductividad (AIT-09-002, 003, 005)
- 1 Analizador ORP (ORP-IT-09-001)

---

## 4. Verificacion vs ET P22-ET-09-000-001-0 (Especificacion Tecnica Modulo)

### 4.1 Codificacion

| Aspecto | Requerido | Entregado | Cumple |
|---------|-----------|-----------|--------|
| Codigo documento | P22-DWG-09-009-XXX | P22-DWG-09-009-002 | **SI** |
| Area (09) | 09 - Osmosis Inversa | 09 | **SI** |
| Tipo (DWG) | DWG - Drawing | DWG | **SI** |

**Veredicto Codificacion:** 1 - Approved

### 4.2 Contenido Tecnico

| Aspecto | Requerido (ET) | Mostrado en P&ID | Cumple |
|---------|----------------|------------------|--------|
| Material tuberias AP | Super Duplex PREN>40 | SSD PREN>40 | **SI** |
| Material turbochargers | Super Duplex 2507 | SDSS 2507 | **SI** |
| Bomba CIP | SS316 | SS316 | **SI** |
| Tanque CIP | HDPE | HDPE | **SI** |
| Filtros cartucho | FRP | FRP | **SI** |
| Instrumentacion conductividad | Requerido | AIT (COND) mostrado | **SI** |
| Instrumentacion ORP | Requerido | AIT (ORP) mostrado | **SI** |
| Instrumentacion temperatura | Requerido | TE/TIT mostrado | **SI** |
| Control valvulas | Tipicos mostrados | V1-V4 definidos | **SI** |
| Control motores | Tipicos mostrados | M1-M4 definidos | **SI** |

**Veredicto Tecnico:** 1 - Approved

---

## 5. Observaciones y Brechas Identificadas

### 5.1 Observaciones CRITICAS (Requieren Accion)

| # | Observacion | Referencia | Impacto |
|---|-------------|-----------|---------|
| 1 | **Presiones turbochargers:** Feed Turbo muestra 63.21 barg, Interstage 77.1 barg. Verificar consistencia con modelaciones de proceso para ambas salinidades. | Asesor LH | ALTO |
| 2 | ~~**Valvulas check:** No se especifica material en P&ID.~~ **CERRADA** - Valvulas check Super Duplex 2507 ya cubiertas por compra directa ADASA (KSB CV421060 Rev.01 - APROBADA). | P22-ET-06-006-001 | ~~MEDIO~~ |
| 3 | **Bomba HP (BH-09-001):** P&ID solo indica VSD. Verificar caudal/TDH/potencia vs datasheet rechazado (P22-ITEM-09-009-002). | Entrega 1 | ALTO |
| 4 | **Margen presion diseno 10%:** P&ID muestra presion maxima operacion 83.9 barg (77.1 + margen). Confirmar que presion de diseno es minimo 85 barg (10% sobre 77.1 barg). | ET Sec 5.1.6 | ALTO |
| 5 | **Transmisores vibracion:** ET Sec 5.5 requiere sensores vibracion en equipos rotativos. Confirmar inclusion en BH-09-001 (HP Pump) y SIP-09-001/002 (Turbochargers). | ET Sec 5.5 | MEDIO |
| 6 | **Analisis flexibilidad:** Solicitar memoria de calculo de flexibilidad para lineas de alta presion (>77 barg). | ET Sec 7 | MEDIO |

### 5.1.1 Observaciones Van Doorn (12-Ene-2026)

| # | Observacion | Referencia | Impacto |
|---|-------------|-----------|---------|
| VD-01 | **Limites de bateria:** Indicar claramente limites de suministro ADASA/BW Water con flanges en todos los puntos de conexion. No estan marcados en el plano. | Van Doorn | MEDIO |
| VD-02 | **Lineas PVC en zona SDSS:** Hay lineas de PVC dentro del rectangulo definido como SDSS (Super Duplex Stainless Steel). Verificar consistencia de materiales o corregir simbologia. | Van Doorn | **ALTO** |
| VD-03 | **TAGs de lineas:** Indicar TAGs de lineas con diametros en todos los tramos. Faltan identificadores en varias lineas. | Van Doorn | MEDIO |
| VD-04 | **Drenaje:** Verificar que corriente indicada va correctamente a drenaje. | Van Doorn | MEDIO |
| VD-05 | **Conexion CIP Tank:** Verificar trazado correcto hacia TK-09-001. Anotacion indica "Va al CIP TANK TK-09-001". | Van Doorn | BAJO |
| VD-06 | **Conexion etapas:** Clarificar que conexion "viene de 1ra y 2da etapa en rigor". | Van Doorn | BAJO |
| VD-07 | **Numeracion TAG:** Verificar secuencia de numeracion - anotacion "3001?" cuestiona consistencia. | Van Doorn | BAJO |
| VD-08 | **Caracteristicas bomba:** Incluir caracteristicas de bomba referenciada en P&ID. Relacionado con Obs. Critica #3 (HP Pump). | Van Doorn | ALTO |

### 5.1.2 Nota Critica sobre Observacion VD-02

> **AUTOCRITICA ADASA:** La observacion VD-02 de Van Doorn (lineas PVC en zona SDSS) identifica una inconsistencia grafica en el P&ID que **NO fue detectada** en la revision ADASA v3.0.

**Analisis:**
- La revision ADASA verifico que la especificacion de materiales en la leyenda del P&ID indica Super Duplex para lineas de alta presion
- Sin embargo, Van Doorn detecto que existen lineas con simbologia PVC dibujadas DENTRO del area demarcada como zona Super Duplex (SDSS)
- Esto representa una inconsistencia entre la leyenda y el diagrama que requiere aclaracion

**Posibles causas:**
1. **Error de simbologia:** Las lineas SDSS estan dibujadas con simbolo PVC incorrecto
2. **Error de demarcacion de zona:** El rectangulo SDSS esta mal dimensionado e incluye lineas de baja presion que SI son PVC
3. **Error de diseno (grave):** BW Water especifico PVC donde deberia ser SDSS

**Accion requerida:** BW Water debe aclarar esta inconsistencia y corregir el P&ID segun corresponda.

**Leccion aprendida:** Futuras revisiones ADASA deben incluir verificacion grafica detallada de consistencia entre leyenda y simbologias del P&ID, no solo verificacion de texto.

### 5.2 Observaciones MENORES (Informativas)

| # | Observacion | Referencia |
|---|-------------|-----------|
| 4 | TIE-IN 5 (Dispersante): Aclarar responsabilidad TK-06-003 - aparece en ADASA pero es suministro BW. | P22-LI-06-005-001 |
| 5 | Transicion de materiales: HDPE externo (ADASA) a SDSS interno (BW) no detallada. | Interfaz |
| 6 | Linea permeado off-spec: PE-HDPE-DN90-PN10-003 en ADASA no visible en P&ID BW. | P22-DWG-06-009-003 |
| 7 | Protocolo comunicacion PLC: Modbus no indicado explicitamente en P&ID. | ET 5.4 |

### 5.3 Verificaciones Positivas

| # | Aspecto | Estado |
|---|---------|--------|
| 1 | Configuracion membranas 6+4 PVs | **COINCIDE** con ADASA |
| 2 | Capacidad 21 m3/h, Recuperacion 42.85% | **COINCIDE** con ADASA |
| 3 | Material turbochargers SDSS 2507 | **CUMPLE** PREN>40 |
| 4 | Instrumentacion conductividad, ORP, temperatura | **INCLUIDA** |
| 5 | Sistema CIP completo (tanque, bomba, heater, filtro) | **INCLUIDO** |

---

## 6. Veredicto Final

| Aspecto | Calificacion | Codigo |
|---------|--------------|--------|
| Cumplimiento Tecnico | Aprobado con notas | 2 |
| Codificacion | Aprobado | 1 |
| Verificacion vs IB ADASA | Aprobado con notas | 2 |
| **VEREDICTO GLOBAL** | **2 - APPROVED AS NOTED** | **2** |

---

## 7. Acciones Requeridas BW Water

| # | Accion | Prioridad | Plazo |
|---|--------|-----------|-------|
| 1 | Confirmar presiones turbochargers corresponden a modelacion actualizada (ambas salinidades) | ALTA | Proxima entrega |
| 2 | ~~Especificar material valvulas check~~ **CERRADA** - Cubierto por compra ADASA | ~~MEDIA~~ | - |
| 3 | Verificar consistencia BH-09-001 vs datasheet corregido | ALTA | Con re-envio datasheet |
| 4 | Aclarar responsabilidad suministro TK-06-003 (Dispersante) | BAJA | Informativo |
| 5 | **NUEVO:** Confirmar presion de diseno minimo 85 barg (margen 10% sobre operacion) | ALTA | Proxima entrega |
| 6 | **NUEVO:** Confirmar sensores vibracion incluidos en BH-09-001 y SIP-09-001/002 | MEDIA | Proxima entrega |
| 7 | **NUEVO:** Entregar memoria calculo flexibilidad lineas alta presion | MEDIA | Previo fabricacion |
| 8 | **VAN DOORN:** Marcar limites de bateria ADASA/BW Water con flanges en plano | ALTA | Proxima revision |
| 9 | **VAN DOORN:** Revisar lineas PVC dentro de zona SDSS - corregir materiales o simbologia | **ALTA** | Proxima revision |
| 10 | **VAN DOORN:** Agregar TAGs de lineas con diametros en todos los tramos | MEDIA | Proxima revision |
| 11 | **VAN DOORN:** Verificar trazado de drenaje y conexion CIP Tank TK-09-001 | MEDIA | Proxima revision |
| 12 | **VAN DOORN:** Clarificar conexion de etapas 1ra y 2da | BAJA | Proxima revision |
| 13 | **VAN DOORN:** Verificar consistencia numeracion TAGs (3001?) | BAJA | Proxima revision |

---

## 8. Documentos de Referencia Utilizados

### Ingenieria Basica ADASA (Area 06)
- P22-DWG-06-009-002: P&ID Alimentacion
- P22-DWG-06-009-003: P&ID OI
- P22-DWG-06-009-004: P&ID CIP
- P22-DWG-06-009-005: P&ID Reactivos
- P22-LI-06-005-001: Lista Equipos Electromecanicos
- P22-LI-06-006-001: Lista de Lineas
- P22-LI-06-006-002: Lista de Valvulas
- P22-LI-06-008-001: Lista de Instrumentos
- P22-ET-06-006-001: ET Canerias y Valvulas

### Especificacion Tecnica Modulo
- P22-ET-09-000-001-0: Especificacion Tecnica Modulo OI

---

## 9. Puntos Ciegos Identificados (Analisis Profundo)

### 9.1 Equipos Nuevos (No en IB Original)

| TAG BW Water | Descripcion | Observacion |
|--------------|-------------|-------------|
| MZE-09-001 | Mezclador Estatico (PVC) | **MEJORA** - Agregado por BW Water para inyeccion antiincrustante |
| REL-09-001 | Calentador CIP (20 kW) | **MEJORA** - No estaba en IB, agrega capacidad de calentamiento para limpieza |

### 9.2 Instrumentacion Adicional (Mejoras BW Water)

| Tipo | IB ADASA | P&ID BW Water | Delta |
|------|----------|---------------|-------|
| Conductivimetros | 1 (salida permeado) | 4 (alimentacion + cada etapa + salida) | **+3** |
| Temperatura | 1 (TK CIP) | 2 (TK CIP + tren RO) | **+1** |
| Switches Nivel | 0 (antiincrustante) | 2 (LS-09-001/002 TK antiincrustante) | **+2** |
| Medidor pH | 0 | 1 (PHIT-09-001 en CIP) | **+1** |

**Nota:** Todas estas adiciones son **mejoras** respecto al diseno base y deben documentarse positivamente.

### 9.3 Puntos Pendientes de Clarificar

| # | Item | Descripcion | Impacto |
|---|------|-------------|---------|
| 1 | Protocolo Modbus TCP | No especificado en P&ID. ET requiere comunicacion Modbus TCP. | **CRITICO** |
| 2 | TDH Bomba HP | Sin detalle en P&ID. IB indica 877 mca (225 kW). | **CRITICO** |
| 3 | Manometro faltante | IB lista 7 PI, P&ID muestra 6. Verificar PI-06-002 (desc. bomba AP). | MEDIO |

### 9.4 Presion de Entrada al Modulo (TIE-IN 1) - Analisis NPSH

**Contexto:** La presion en TIE-IN 1 (entrada salmuera al modulo) es critica porque constituye el NPSH disponible para la bomba de alta presion BH-09-001.

#### Requerimiento BW Water

| Parametro | Valor | Fuente |
|-----------|-------|--------|
| Presion minima TIE-IN 1 | **3 bar (45 psi)** | Oferta Tecnica Rev.1, Sec. Operating Requirements |
| Caudal alimentacion | 48.22 m3/h | P&ID Entrega 3 |

**Nota:** Esta presion minima corresponde al NPSH requerido por la bomba de alta presion para evitar cavitacion.

#### Especificacion ADASA (ET P22-ET-09-000-001-0)

Seccion 5.6 indica: *"Tie-in 1: La presion que debera entregar ADASA en este punto debera ser informada por el Oferente en su oferta."*

**Conclusion:** BW Water informo que requiere minimo **3 bar** en su oferta, quedando como compromiso de ADASA garantizar esta presion.

#### Verificacion vs Bomba Alimentacion KSB (BH-06-001)

**Referencia:** Oferta KSB CV406762-REV1 (29-Dic-2025)

| Parametro | IB ADASA (P22-ET-06-005-001) | Oferta KSB | Estado |
|-----------|------------------------------|------------|--------|
| Modelo | Por proveedor | KNCPP 5A M 11-050 | - |
| Caudal | 48.2 m3/h | 48.22 m3/h | **CUMPLE** |
| TDH | 40 m.c.a. | 40.03 m.c.a. | **CUMPLE** |
| Potencia | Por proveedor | 11 kW | - |
| NPSH requerido | - | 2.64 m.c.a. | OK |

#### Balance de Presion Estimado

| Concepto | Valor | Nota |
|----------|-------|------|
| Presion generada bomba KSB | ~4.1 bar | TDH 40 mca @ densidad 1.05 |
| Perdidas canerias HDPE (~150m) | -0.3 a -0.5 bar | Estimado |
| Perdidas accesorios/valvulas | -0.2 a -0.3 bar | Estimado |
| **Presion disponible TIE-IN 1** | **~3.3 a 3.6 bar** | |
| **Requerimiento minimo BW Water** | **3.0 bar** | |
| **Margen** | **+0.3 a +0.6 bar** | **MARGINAL** |

#### Veredicto Presion de Entrada

| Aspecto | Estado | Comentario |
|---------|--------|------------|
| Bomba KSB cumple TDH especificado IB | **SI** | 40.03 mca vs 40 mca |
| Presion disponible >= 3 bar | **SI (marginal)** | ~3.3-3.6 bar estimado |
| Margen de seguridad adecuado | **BAJO** | Solo 10-20% de reserva |

#### Acciones Requeridas

| # | Accion | Responsable | Prioridad |
|---|--------|-------------|-----------|
| 1 | Confirmar con BW Water que 3 bar es presion minima absoluta o si hay tolerancia | ADASA | **ALTA** |
| 2 | Solicitar calculo hidraulico definitivo de perdidas canerias TK-06-001 a TIE-IN 1 | Ingenieria | MEDIA |
| 3 | Evaluar si es necesario sobre-dimensionar TDH de bomba (45-50 mca) para mayor margen | ADASA | MEDIA |

**Conclusion:** La bomba KSB ofertada cumple con la IB ADASA (40 mca), pero el margen respecto al requerimiento de 3 bar de BW Water es ajustado. Se recomienda confirmar tolerancia con BW Water y realizar calculo hidraulico definitivo.

---

## 10. Brechas Cerradas (Revision Critica v3.0)

### 10.1 Acoples Victaulic - CERRADA

**Observacion original:** "Acoples Victaulic sin justificacion tecnica para uso en alta presion"

**Resolucion:** BW Water incluyo justificacion completa en **Oferta Tecnica Rev.1, Seccion 13**:

| Parametro | Victaulic PIEDMONT | Operacion Maxima | Evaluacion |
|-----------|-------------------|------------------|------------|
| Rating | 2000 PSI (138 bar) | 83.9 barg | **CUMPLE** |
| Margen sobre operacion | **64%** | - | **ADECUADO** |
| Material housing | CE3MN (Superduplex) ASTM A995 | PREN>40 requerido | **CUMPLE** |
| Sello | EPDM grado EW | - | **CUMPLE ET** |
| Presion prueba | 3000 PSI (207 bar) | - | **SUPERA** |

**Veredicto:** Los acoples Victaulic cumplen holgadamente para operacion a 84 barg. Margen 64% supera el 10% requerido. **NO REQUIERE ACCION ADICIONAL.**

### 10.2 Valvulas Check Super Duplex - CERRADA

**Observacion original:** "Material valvulas check no especificado en P&ID"

**Resolucion:** Valvulas check son suministro ADASA, no BW Water. Proceso de compra completado:

| Documento | Codigo | Estado |
|-----------|--------|--------|
| Oferta KSB | CV421060 Rev.01 | **APROBADA** |
| Material | Super Duplex 2507 | **CUMPLE PREN>40** |
| Cantidad | 4 unidades DN100 | Listo para OC |

**Veredicto:** Valvulas check cubiertas por compra directa ADASA. **NO REQUIERE ACCION BW Water.**

---

## 11. Coordinacion con COMPRA EQUIPOS ADASA

### 11.1 Estado de Compras Relacionadas

| Equipo | Proveedor | Oferta | Estado | Observacion |
|--------|-----------|--------|--------|-------------|
| Valvulas Check DN100 | KSB Chile | CV421060 Rev.01 | **APROBADA** | Super Duplex 2507 - Lista para OC |
| Bomba Alimentacion BH-06-001 | KSB Chile | CV406762-REV1 | **EN EVALUACION** | Material aceptado (ver 11.2) |
| Bomba Sumergible BS-06-001 | KSB Chile | CV406762-REV1 | **EN EVALUACION** | Material aceptado (ver 11.2) |

### 11.2 Decision Material Bombas KSB

**Decision ADASA (06-Ene-2026):** Se acepta Duplex (1.4462, 1.4517) en componentes de baja presion.

**Justificacion:**
- Bombas BH-06-001 y BS-06-001 operan a **4-10 bar** (baja presion)
- A estas presiones y temperatura moderada (13-22°C), Duplex es adecuado
- Riesgo de corrosion bajo tension (SCC) es significativamente menor que en alta presion

| Bomba | Componente | Material KSB | PREN | Estado |
|-------|------------|--------------|------|--------|
| BH-06-001 | Carcasa/Impulsor | A995 GR 5A (Superduplex) | ~42 | **CUMPLE** |
| BH-06-001 | Eje | 1.4462 (Duplex) | ~34 | **ACEPTADO** |
| BS-06-001 | Carcasa/Impulsor | 1.4517 (Duplex) | ~35 | **ACEPTADO** |
| BS-06-001 | Eje | 1.4462 (Duplex) | ~34 | **ACEPTADO** |

**Comparacion con modulo BW Water:**
- Turbochargers BW Water: Superduplex 2507 @ 77-84 barg - **Correcto para alta presion**
- Bombas KSB: Duplex/Superduplex mixto @ 4-10 barg - **Aceptable para baja presion**

### 11.3 Acciones Pendientes COMPRA EQUIPOS

| # | Accion | Responsable | Estado |
|---|--------|-------------|--------|
| 1 | Emitir OC valvulas KSB CV421060 Rev.01 | ADASA Compras | Listo |
| 2 | Validar calculo hidraulico TK-06-001 a TIE-IN 1 | Ingenieria | Pendiente |
| 3 | Confirmar compatibilidad VFD con motor KSB IE3 | ADASA Compras | Pendiente |

---

## 12. Comparacion con Revisiones Anteriores

| Aspecto | Revision v2.0 | Revision v3.0 | Revision v3.1 | Revision v3.2 |
|---------|---------------|---------------|---------------|---------------|
| Cruce vs IB ADASA | SI | SI | SI | SI |
| Revision critica comentarios | No | SI | SI | SI |
| Coordinacion COMPRA EQUIPOS | No | SI | SI | SI |
| Brechas cerradas documentadas | No | SI (2) | SI (2) | SI (2) |
| **Revision Van Doorn** | No | No | **SI** | **SI** |
| **Analisis de inconsistencias** | No | No | No | **SI** |
| Observaciones criticas ADASA | 3 | 6 (1 cerrada + 5 activas) | 6 (1 cerrada + 5 activas) | 6 (1 cerrada + 5 activas) |
| **Observaciones Van Doorn** | - | - | **8** | **8** |
| **Nota autocritica ADASA** | - | - | - | **SI (VD-02)** |
| Veredicto | 2 - Approved as noted | 2 - Approved as noted | 2 - Approved as noted | 2 - Approved as noted |

---

**Firma Revisor:** _____________________
**Fecha:** 12-Ene-2026

---

*Documento generado: 12-Ene-2026*
*Version: 3.2 - Incluye analisis critico de inconsistencias Van Doorn vs ADASA*
*Nota: Se agrega seccion 5.1.2 con autocritica sobre observacion VD-02 no detectada por ADASA*
