# Registro de Compromisos — P22-IT-06-000-006-0

Seguimiento de los compromisos vivos del Contrato C-4300, de las dos partes. Es administración de contrato, no revisión documental: el Master Register (`REVISIONES/EVALUACIONES/P22-IT-06-000-002-0`) sigue entregables y veredictos, este registro sigue **quién debe qué, para cuándo y con qué respaldo se puede exigir**.

## Cómo se usa

```
compromisos.yaml            FUENTE ÚNICA — se edita esto
hitos.yaml                  FUENTE ÚNICA — ventanas del programa
generar_excel_compromisos.py    lee los YAML, valida y escribe el .xlsx
exportar_pdf_excel.py           gate visual (Excel COM)
P22-IT-06-000-006-0_Registro-de-Compromisos.xlsx    DERIVADO — no se edita
_backups/                   copia previa automática en cada regeneración
```

```bash
python generar_excel_compromisos.py     # valida, respalda y regenera
python exportar_pdf_excel.py            # render de control -> *_VISTA.pdf
```

**El `.xlsx` nunca se edita a mano.** Cualquier cambio manual se pierde en la siguiente corrida. Un cambio de estado se escribe en el YAML, se regenera y queda versionado en git junto al resto del proyecto.

## Las dos decisiones de diseño que importan

**Lo que cambia por un evento va como valor; lo que cambia por el paso del tiempo va como fórmula.** El `Estado` de un compromiso lo mueve un hecho (llegó el documento, se firmó la carta) y por eso es un valor del YAML. El `Semáforo` y los `Días vs. compromiso` los mueve el calendario, y por eso son fórmulas con `TODAY()` y el color lo pone el formato condicional. Un relleno fijado al generar sería correcto el día de la corrida y falso al siguiente: es el modo de falla silencioso de estos registros.

**Ninguna fecha se infiere.** Una fuente que dice "próxima semana" u "once ready" produce `SIN FECHA`, que se colorea igual que las demás. Un compromiso sin vencimiento es un defecto de gestión, no un estado neutro — al corte inicial son 21 de 59, más de un tercio.

## Las dos columnas que hacen el trabajo pesado

**`Origen de la fecha`** dice de antemano con qué munición se puede reclamar. `CONTRACTUAL` se cita con consecuencia: el Plazo de Entrega es la Cláusula 27 de la BAE y su incumplimiento activa la 43.1 letra b). `COMPROMISO VERBAL-MINUTA` solo se recuerda: el "shipment readiness 21-Sep" es una frase de una minuta que ADASA nunca aceptó, y tratarlo como fecha exigible sería un error de encuadre. La distinción existe porque ya costó caro una vez, cuando hubo que reencuadrar el reclamo del dossier sobre la ET Sección 7 al descubrir que el "24-Jul" no constaba por escrito.

**`Reprogramaciones`** convierte en número lo que de otro modo queda disuelto en prosa. La cotización de repuestos lleva 22-Jun, 03-Jul, 10-Jul y 31-Jul: ese 3 es la prueba objetiva de un patrón, no una impresión. La hoja `Movimientos` lista solo los compromisos que se movieron, ordenados por número de desplazamientos, y es lo que convierte el registro en evidencia utilizable.

## Gates antes de distribuir

1. `validar_fuente()` **aborta** la generación (no advierte) ante vocabulario fuera de lista, id duplicado, fecha que no es fecha, referencia cruzada inexistente, o incoherencia entre estado y fecha de cierre.
2. `python3 ~/.claude/skills/_shared/openpyxl_lint.py` sobre el `.py` y sobre el `.xlsx`, exit 0.
3. Render con **Excel real**, nunca con LibreOffice: openpyxl escribe las fórmulas sin valor cacheado y LibreOffice abre los `.xlsx` con el recálculo desactivado, de modo que mostraría vacías las columnas de Semáforo y Días y llevaría a diagnosticar un defecto inexistente.

Sobre el punto 3 hay un gotcha propio de este archivo, ya corregido y documentado en el código: en un estilo diferencial (`dxf`) Excel toma el color de `bgColor`, no de `start_color`. Un `PatternFill` construido con `start_color` produce una regla que se aplica sin pintar nada. El defecto solo se ve al renderizar — inspeccionar el archivo no lo revela.

## Regla anti-contradicción

Si el README del proyecto y este registro discrepan en una fecha vigente, **manda el registro**. Una fecha nunca se escribe dos veces como estado vivo: el README lleva la Bitácora de lo que ocurrió, el registro lleva lo que está pendiente.

El generador imprime al terminar la línea de agregados lista para pegar en el `Estado Vigente` del README.
