#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la planilla que acompana al paquete `INGENIERIA VIGENTE PARA CONSTRUCCION` del
montaje mecanico y las obras civiles de Taltal. Se entrega al contratista adjudicado.

Responde dos preguntas: que ingenieria rige hoy y que cambio respecto de la que se uso
para cotizar.

Fuente unica: este script. El .xlsx es derivado y no se edita a mano.

Desde el 09-09-2026 el .xlsx es RESPALDO INTERNO y no viaja en el paquete: la Nota
Tecnica P22-NT-06-000-001-0 lo absorbio y es el unico documento de control que se
entrega. Este script se mantiene por dos razones: sus listas VIGENCIA y CUBICACIONES
son la fuente que el generador de la nota importa, y su gate contrasta lo declarado
contra el arbol real del paquete antes de escribir nada.
Todos los datos estan verificados contra los archivos, no contra las cartas de remision.

La hoja Vigencia se contrasta contra el arbol real del paquete antes de escribir: si un
codigo declarado no tiene archivo, o lo tiene en otra revision, el script aborta.

Las partidas se citan con la numeracion del Formato de Presupuesto contractual. Ese
Formato repite dos codigos (dos 4.3 y dos 4.7), por lo que toda referencia va por numero
y nombre completo de la partida.
"""
from pathlib import Path
import re
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

BASE = Path(__file__).resolve().parent.parent
SALIDA = BASE / "P22-LI-06-000-002-1_Ingenieria-Vigente-y-Cambios.xlsx"
PAQUETE = BASE.parent / "INGENIERIA VIGENTE PARA CONSTRUCCION"
# Indice del paquete, en su raiz. Lo escribe generar_indice_paquete.py y no es un documento
# de la hoja Vigencia.
INDICE = "00_INDICE DEL PAQUETE.xlsx"

FUENTE = "Aptos Narrow"
AZUL = PatternFill("solid", start_color="FF1F3864", end_color="FF1F3864")
GRIS = PatternFill("solid", start_color="FFD9D9D9", end_color="FFD9D9D9")
AMAR = PatternFill("solid", start_color="FFFFF2CC", end_color="FFFFF2CC")
FINO = Side(style="thin", color="FF808080")
BORDE = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)

# --------------------------------------------------------- partidas del Formato
# Numeracion literal del Formato de Presupuesto contractual, con los dos codigos que
# el Formato repite marcados como (a) y (b). El nombre es el que gobierna la cita.
P_CONTENEDOR = "4.1 Fundacion contenedor modulo RO (F2)"
P_CIP = "4.2 Fundacion sistema CIP (F2b)"
P_CUBIERTA = "4.3 Fundacion de la cubierta metalica del sistema CIP (cobertizo)"
P_BOMBA = "4.3 Fundacion dinamica bomba BH-06-001 (F3)"
P_ESTANQUE = "4.4 Fundacion estanque TK-06-001 (F4)"
P_FOSA = "4.5 Fundacion camara de drenajes TK-06-004 (F5)"
P_EXCAV = "4.6 Excavacion comun en fundaciones y zanjas de drenaje"
P_DADOS = "4.7 Dados de hormigon G25 para pedestales de soportes a piso"
P_RELLENO = "4.7 Relleno compactado con material seleccionado y base estabilizada"
P_DRENAJE = "4.8 Sistema de drenaje del modulo"
P_CAMARAS = "4.9 Camaras de inspeccion prefabricadas"
P_INSERTOS = "4.10 Insertos y estructura embebida del contenedor RO"
P_IMP_FOSA = "4.11 Impermeabilizacion quimico-resistente interior de la fosa TK-06-004"
P_IMP_HORM = "4.12 Impermeabilizacion y proteccion del hormigon enterrado"

# --------------------------------------------------------------------------- datos
MECANICA = [
    # codigo, lamina/hoja, titulo, rev cotizada, rev vigente, origen, que cambio, afecta, partida
    ("P22-DWG-06-005-103", "unica", "Plano de montaje del modulo de desalacion", "0", "1",
     "Nota de Envio N16, 25-08-2026",
     "El modulo sube 250 mm: la fundacion pasa de la cota +6,050 a +6,300. Cambios en la planta y en la banda de elevacion.",
     "Si", "Capitulo 1, todas las lineas"),
    ("P22-DWG-06-006-101", "unica", "Plano de cañerias de interconexiones, planta", "0", "1",
     "Nota de Envio N16, 25-08-2026",
     "Trazado actualizado en seis zonas de la planta.",
     "Si", "Capitulo 1, todas las lineas"),
    ("P22-DWG-06-006-102", "unica", "Plano de cañerias de interconexiones, cortes y detalles", "0", "1",
     "Nota de Envio N16, 25-08-2026",
     "Corte A redibujado con las cotas nuevas de tie-in: P8-001 de +8,250 a +8,500; P9-001 y P9-002 de +8,593 a +8,850; P9-003 de +8,583 a +8,850. Los equipos del sistema CIP pasan de bloque esquematico a detalle. En el Corte D desaparece la valvula VM-06-010, que la revision anterior rotulaba como proyectada y que no tiene partida en el Formato. Los tie-ins 1, 3 y 6 con el Modulo 3 mantienen su cota +6,204.",
     "Si", "Capitulo 1, lineas de interconexion"),
    ("P22-DWG-06-006-103", "unica", "Plano de cañerias TK y bomba de salmuera, planta", "0", "1",
     "Nota de Envio N15, 17-07-2026",
     "Emitido para construccion en la revision 1.",
     "Si", "Capitulo 1, lineas del estanque y la bomba"),
    ("P22-DWG-06-006-104", "unica", "Plano de cañerias TK y bomba de salmuera, cortes y detalles", "0", "1",
     "Nota de Envio N15, 17-07-2026", "Re-emision acompanando a la planta.",
     "Si", "Capitulo 1, lineas del estanque y la bomba"),
    ("P22-DWG-06-006-005", "H.1 a H.5", "Isometria linea SA-HDPE-DN110-PN10-005", "0 (4 hojas)", "2 (5 hojas)",
     "Notas de Envio N15 y N17", "Una hoja mas que la revision con la que se cotizo (5 hojas contra 4). Las cuatro hojas de la revision cotizada mantienen su numero.",
     "Si", "Capitulo 1, item 1.6"),
    ("P22-DWG-06-006-008", "H.1 a H.5", "Isometria linea PE-HDPE-DN90-PN10-001", "0 (4 hojas)", "1 (5 hojas)",
     "Nota de Envio N17, 31-08-2026", "Entra una hoja nueva en la posicion H.4, por lo que la antigua H.4 pasa a ser H.5. Comparar contra la revision cotizada por contenido, no por numero de hoja.",
     "Si", "Capitulo 1, item 1.10"),
    ("P22-DWG-06-006-009", "H.1 y H.2", "Isometria linea PE-HDPE-DN90-PN10-003", "0", "1",
     "Nota de Envio N17, 31-08-2026", "Mismo numero de hojas y misma numeracion. Cambios menores en el cuadro de materiales.",
     "Si", "Capitulo 1, item 1.12"),
    ("P22-DWG-06-006-011", "H.1 a H.8", "Isometria linea SA-HDPE-DN110-PN10-007", "0 (7 hojas)", "2 (8 hojas)",
     "Notas de Envio N15 y N17", "Entra una hoja nueva en la posicion H.2 y las seis siguientes se desplazan: la H.2 de la revision cotizada es ahora la H.3, y la H.7 es la H.8. SEIS DE SIETE HOJAS CAMBIAN DE NUMERO. Comparar contra la revision cotizada por contenido, nunca por numero de hoja.",
     "Si", "Capitulo 1, item 1.7"),
    ("P22-LI-06-006-102", "-", "Listado de materiales de cañerias", "0", "1",
     "Nota de Envio N15, 17-07-2026",
     "La cañeria no cambia: 335 m en total, y tampoco cambian codos, cuplas, tee, reducciones, esparragos ni stub end. Salen los dos accesorios de PVC-U (codo 90 grados 4 pulgadas y tee reductora 4x2), con lo que la instalacion queda integra en HDPE. La brida es la misma pieza (un flange suelto de junta solapada sobre stub end, LJ = Lap Joint, con perforaciones ASME B16.5 clase 150 en las dos revisiones): lo que la revision 1 incorpora es su MATERIAL, acero galvanizado por inmersion, y el de 4 pulgadas pasa de 22 a 23 unidades. El buje de reduccion Super Duplex UNS S32750 sube de 2 a 5 unidades y el spigot saddle with cutter 4x1 de 2 a 5. Entra la union adaptador PE100 por Super Duplex de 1 pulgada, 3 unidades. Sale el back-up flange de 4 pulgadas. Las empaquetaduras bajan de 45 a 42 unidades.",
     "Si", "Capitulo 1, todas las lineas"),
    ("P22-LI-06-008-101", "-", "Listado de instrumentos", "0", "1",
     "Nota de Envio N15, 17-07-2026", "Actualizacion del listado.",
     "No", "-"),
    ("P22-DWG-06-009-102", "-", "P&ID de alimentacion", "0", "1 no incorporada",
     "Nota de Envio N15, 17-07-2026",
     "Rige la revision 0 en PDF y DWG. La revision 1 existe solo como DWG en la NE 15 y no entra al paquete: un nativo no viaja en una revision distinta a la de su PDF (registro interno; pedir el ploteo a Van Doorn).",
     "No", "-"),
]

CIVIL_CAMBIA = [
    ("P22-DWG-00-002-002", "LAM1", "Fundaciones de equipos exteriores, fundacion del estanque TK-06-001", "0", "1",
     "Carta 067-032-032-COR-TT-016, 10-09-2026 (reemite la Rev 1 de la carta TT-013, 03-09-2026)",
     "Cubicacion de hormigon identica: 6,03 m3 de G25 y 0,50 m3 de G10. La excavacion sube de 4,22 a 4,84 m3 y el retiro de 5,06 a 5,81, porque el fondo de excavacion baja al sello +5,350 menos el emplantillado de 5 cm, en coherencia con el plano de movimiento de tierra.",
     "Si", P_ESTANQUE + " (cantidad sin cambio) y " + P_EXCAV),
    ("P22-DWG-00-002-002", "LAM4", "Fundaciones de equipos exteriores, fundacion de la bomba BH-06-001", "0", "1",
     "Carta 067-032-032-COR-TT-013, 03-09-2026",
     "Solo fecha del cajetin. Cubicacion identica: 0,95 m3 de G25, excavacion 0,62 m3 y retiro 0,75 m3.",
     "No", P_BOMBA),
    ("P22-DWG-00-002-003", "LAM1", "Fundacion del contenedor del modulo, formas", "0", "1",
     "Carta 067-032-032-COR-TT-016, 10-09-2026 (reemite la Rev 1 de la carta TT-013, 03-09-2026)",
     "Las cotas suben 250 mm: cara superior de +6,050 a +6,300 y sello de +5,150 a +5,400. Geometria y armadura iguales: diez pedestales de 1,00 x 1,00 m en cinco ejes separados 3,00 m, unidos por vigas de 30 x 30 cm. Hormigon sin cambio: 7,52 m3 de G25 y 0,83 m3 de G10. El cuadro de excavacion se dimensiona sobre el sello nuevo: excavacion de 38,02 a 20,95 m3, retiro de 45,62 a 25,14 y relleno de 30,03 a 13,96, coincidente con el plano de movimiento de tierra.",
     "Si", P_CONTENEDOR + " (cantidad sin cambio) y " + P_EXCAV),
    ("P22-DWG-00-002-007", "LAM1", "Fundacion del sistema CIP, formas", "0", "1",
     "Carta 067-032-032-COR-TT-016, 10-09-2026 (reemite la Rev 1 de la carta TT-013, 03-09-2026)",
     "La fundacion de los equipos se rediseña y se reduce de 4,13 a 2,63 m3 de G25. Entra una junta de dilatacion entre elementos de fundacion: poliestireno expandido de 2,5 cm, sello Sikaflex 1A y primer VP-215 en ambas paredes. El total de G25 de la zona baja de 7,36 a 5,80 m3 y la excavacion de 5,01 a 1,03 m3 (retiro 1,24), coincidente con el plano de movimiento de tierra. La disposicion y las dimensiones de los pernos de anclaje quedan definidas.",
     "Si", P_CIP + " y " + P_EXCAV),
    ("P22-DWG-00-002-007", "LAM2", "Fundacion del sistema CIP, armaduras", "0", "1",
     "Carta 067-032-032-COR-TT-013, 03-09-2026",
     "Armadura renumerada completa: las marcas 1201 a 1204 pasan a 1211 a 1216, con cantidades y largos distintos.",
     "No", P_CIP + " (incluida en el m3)"),
    ("P22-DWG-00-002-001", "LAM1", "Implantacion general de obras civiles, planta georeferenciada y cortes", "0", "1",
     "Carta 067-032-032-COR-TT-014, 07-09-2026",
     "Actualiza las coordenadas UTM de once de los trece vertices de replanteo. El mayor desplazamiento es el del vertice V13, de Norte 7.188.940,939 Este 350.112,089 a Norte 7.188.940,098 Este 350.118,124, unos 6 m en el Este. Los vertices V04 y V05 no cambian. El nivel de terreno natural por zona se mantiene.",
     "Si", "Replanteo de todas las partidas del Capitulo 4"),
    ("P22-DWG-00-001-001", "LAM1", "Excavaciones y movimiento de tierras, planta general", "0", "1",
     "Carta 067-032-032-COR-TT-016, 10-09-2026 (reemite la Rev 1 de la carta TT-015, 08-09-2026)",
     "El cuadro de cubicaciones pasa de ocho a diez items y recoge el sello nuevo: la excavacion del contenedor baja de 38,02 a 20,95 m3 sobre un area que pasa de 53,51 a 49,96 m2, la de la zona CIP de 5,01 a 1,03 m3, y la del estanque sube de 4,22 a 4,84 m3. Entran la excavacion de la fundacion de la bomba BH-06-001, 0,62 m3, y la de la fundacion de la cubierta del sistema CIP, 4,25 m3. Todas las cifras coinciden con el cuadro del plano de fundacion de su zona. Los rellenos del trazado no cambian.",
     "Si", P_EXCAV),
    ("P22-DWG-00-001-001", "LAM2", "Excavaciones y movimiento de tierras, secciones y detalle", "0", "1",
     "Carta 067-032-032-COR-TT-016, 10-09-2026 (reemite la Rev 1 de la carta TT-015, 08-09-2026)",
     "El fondo de excavacion del contenedor sube de EL. 5,15 a EL. 5,35 y el del estanque baja de EL. 5,35 a EL. 5,30, cada uno igual a su sello de fundacion menos el emplantillado de 5 cm. En la fosa TK-06-004 la seccion B acota EL. 4,30, el sello +4,305 del P22-DWG-00-002-004 LAM1 redondeado; bajo ese sello va emplantillado de 5 cm, no mejoramiento: el rotulo M.H.A. e=15 de ese plano es el muro de hormigon armado de la fosa.",
     "Si", P_EXCAV),
]

# Cantidades del Formato de Presupuesto contractual contra la ingenieria vigente.
# El primer campo es el numero literal de la partida en el Formato; los codigos 4.3 y
# 4.7 aparecen dos veces porque el Formato los repite.
CUBICACIONES = [
    ("4.1", "Fundacion contenedor modulo RO (F2)", "m3", 7.52, 7.52, "P22-DWG-00-002-003 LAM1 Rev 1"),
    ("4.2", "Fundacion sistema CIP (F2b)", "m3", 7.36, 5.80, "P22-DWG-00-002-007 LAM1 Rev 1"),
    ("4.3", "Fundacion de la cubierta metalica del sistema CIP (cobertizo)", "m3", 2.38, 2.38, "P22-DWG-00-002-007 LAM3 Rev 0"),
    ("4.3", "Fundacion dinamica bomba BH-06-001 (F3)", "m3", 0.95, 0.95, "P22-DWG-00-002-002 LAM4 Rev 1"),
    ("4.4", "Fundacion estanque TK-06-001 (F4)", "m3", 6.33, 6.33, "P22-DWG-00-002-002 LAM1 Rev 1"),
    ("4.5", "Fundacion camara de drenajes TK-06-004 (F5)", "m3", 1.66, 1.66, "P22-DWG-00-002-004 Rev 0"),
    ("4.6", "Excavacion comun en fundaciones y zanjas de drenaje", "m3", 115.1, 90.64, "P22-DWG-00-001-001 LAM1 Rev 1 y cuadros de excavacion de los planos de fundacion"),
    ("4.7", "Dados de hormigon G25 para pedestales de soportes a piso", "un", 17, 17, "P22-DWG-06-006-107 Rev 0"),
    ("4.7", "Relleno compactado con material seleccionado y base estabilizada", "m3", 91.5, 91.5, "Referencial del itemizado del proyectista; se mide por obra ejecutada"),
    ("4.8", "Sistema de drenaje del modulo", "gl", 1, 1, "P22-DWG-00-002-006 Rev 0"),
    ("4.9", "Camaras de inspeccion prefabricadas", "un", 6, 6, "P22-DWG-00-002-006 Rev 0"),
    ("4.10", "Insertos y estructura embebida del contenedor RO", "kg", 405.66, 405.66, "P22-DWG-00-002-003 LAM2 Rev 0"),
    ("4.11", "Impermeabilizacion quimico-resistente interior de la fosa TK-06-004", "gl", 1, 1, "Referencial"),
    ("4.12", "Impermeabilizacion y proteccion del hormigon enterrado", "gl", 1, 1, "Referencial"),
]

# Revision que rige para cada documento del paquete. Se contrasta contra el arbol real
# antes de escribir la planilla (ver comprobar_vigencia_contra_paquete).
# (codigo, lamina u hoja, titulo, revision vigente, dossier)
D_MEC = "1. ING. DETALLE MECANICA"
D_CIV = "2. OBRAS CIVILES"
D_ETM = "3. ET MONTAJE"
D_SIT = "4. SITIO"
D_EQU = "5. EQUIPOS"

VIGENCIA = [
    ("P22-LI-06-000-101", "-", "Listado de entregables de ingeniería mecánica", "0", D_MEC),
    ("P22-DWG-06-009-101", "única", "Diagrama de flujo de proceso", "0", D_MEC),
    ("P22-DWG-06-009-102", "única", "P&ID de alimentación al módulo", "0", D_MEC),
    ("P22-DWG-06-009-103", "única", "P&ID de ósmosis inversa, sistema de tratamiento de salmuera", "0", D_MEC),
    ("P22-DWG-06-009-104", "única", "P&ID del sistema CIP", "0", D_MEC),
    ("P22-DWG-06-009-105", "única", "P&ID de reactivos", "0", D_MEC),
    ("P22-ET-06-008-101", "-", "Hojas de datos de instrumentos", "0", D_MEC),
    ("P22-IT-06-008-101", "-", "Lógica de control", "0", D_MEC),
    ("P22-LI-06-008-101", "-", "Listado de instrumentos", "1", D_MEC),
    ("P22-DWG-06-005-101", "única", "Plano de montaje del estanque y la bomba de salmuera", "0", D_MEC),
    ("P22-DWG-06-005-102", "única", "Plano de implantación general", "0", D_MEC),
    ("P22-DWG-06-005-103", "única", "Plano de montaje del módulo de desalación", "1", D_MEC),
    ("P22-DWG-06-005-104", "única", "Plano de drenajes", "0", D_MEC),
    ("P22-DWG-06-005-105", "única", "Plano de montaje de la fosa de drenajes", "0", D_MEC),
    ("P22-LI-06-005-101", "-", "Listado de equipos", "0", D_MEC),
    ("P22-DWG-06-006-001", "H.1 y H.2", "Isometría línea SA-HDPE-DN110-PN10-001", "0", D_MEC),
    ("P22-DWG-06-006-002", "H.1 a H.4", "Isometría línea SA-HDPE-DN110-PN10-002", "0", D_MEC),
    ("P22-DWG-06-006-003", "única", "Isometría línea SA-HDPE-DN63-PN10-001", "0", D_MEC),
    ("P22-DWG-06-006-004", "única", "Isometría línea SA-HDPE-DN110-PN10-004", "0", D_MEC),
    ("P22-DWG-06-006-005", "H.1 a H.5", "Isometría línea SA-HDPE-DN110-PN10-005", "2", D_MEC),
    ("P22-DWG-06-006-006", "única", "Isometría línea SA-HDPE-DN110-PN10-003", "0", D_MEC),
    ("P22-DWG-06-006-008", "H.1 a H.5", "Isometría línea PE-HDPE-DN90-PN10-001", "1", D_MEC),
    ("P22-DWG-06-006-009", "H.1 y H.2", "Isometría línea PE-HDPE-DN90-PN10-003", "1", D_MEC),
    ("P22-DWG-06-006-010", "única", "Isometría línea PE-HDPE-DN90-PN10-002", "sin sufijo de revision", D_MEC),
    ("P22-DWG-06-006-011", "H.1 a H.8", "Isometría línea SA-HDPE-DN110-PN10-007", "2", D_MEC),
    ("P22-DWG-06-006-012", "única", "Isometría línea PE-HDPE-DN110-PN10-003", "sin sufijo de revision", D_MEC),
    ("P22-DWG-06-006-101", "única", "Plano de cañerías de interconexiones, planta", "1", D_MEC),
    ("P22-DWG-06-006-102", "única", "Plano de cañerías de interconexiones, cortes y detalles", "1", D_MEC),
    ("P22-DWG-06-006-103", "única", "Plano de cañerías TK y bomba de salmuera, planta", "1", D_MEC),
    ("P22-DWG-06-006-104", "única", "Plano de cañerías TK y bomba de salmuera, cortes y detalles", "1", D_MEC),
    ("P22-DWG-06-006-105", "única", "Plano de ubicación de soportes, planta de interconexiones", "0", D_MEC),
    ("P22-DWG-06-006-106", "única", "Plano de ubicación de soportes, TK y bomba, cortes", "0", D_MEC),
    ("P22-DWG-06-006-107", "21 páginas", "Cuadernillo de soportes", "0", D_MEC),
    ("P22-ET-06-006-001", "-", "Especificación técnica de cañerías de fabricación", "0", D_MEC),
    ("P22-LI-06-006-101", "-", "Listado de líneas", "0", D_MEC),
    ("P22-LI-06-006-102", "-", "Listado de materiales de cañerías", "1", D_MEC),
    ("P22-LI-06-006-103", "-", "Listado de válvulas", "0", D_MEC),
    ("MODULO COMPLETO.nwd", "-", "Modelo 3D de coordinación, Navisworks", "-", D_MEC),
    ("MODULO COMPLETO (nube puntos).nwd", "-", "Modelo 3D con la nube de puntos del levantamiento, Navisworks", "-", D_MEC),
    ("P22-DWG-00-001-001", "LAM1 y LAM2", "Excavaciones y movimiento de tierras", "1", D_CIV),
    ("P22-DWG-00-002-001", "única", "Implantación general de obras civiles", "1", D_CIV),
    ("P22-DWG-00-002-002", "LAM1", "Fundación del estanque TK-06-001, formas", "1", D_CIV),
    ("P22-DWG-00-002-002", "LAM2 y LAM3", "Fundaciones de equipos exteriores, armaduras", "0", D_CIV),
    ("P22-DWG-00-002-002", "LAM4", "Fundación de la bomba BH-06-001", "1", D_CIV),
    ("P22-DWG-00-002-003", "LAM1", "Fundación del contenedor del módulo, formas", "1", D_CIV),
    ("P22-DWG-00-002-003", "LAM2 y LAM3", "Fundación del contenedor, armaduras y anclajes", "0", D_CIV),
    ("P22-DWG-00-002-004", "LAM1 y LAM2", "Fosa de drenajes TK-06-004", "0", D_CIV),
    ("P22-DWG-00-002-006", "LAM1, LAM2 y LAM3", "Canalizaciones y red de drenajes", "0", D_CIV),
    ("P22-DWG-00-002-007", "LAM1", "Fundación del sistema CIP, formas", "1", D_CIV),
    ("P22-DWG-00-002-007", "LAM2", "Fundación del sistema CIP, armaduras", "1", D_CIV),
    ("P22-DWG-00-002-007", "LAM3", "Fundación de la cubierta del sistema CIP", "0", D_CIV),
    ("P22-ET-00-010-101", "-", "Especificación técnica de movimiento de tierra", "1", D_CIV),
    ("P22-ET-00-010-102", "-", "Especificación técnica de obras civiles", "1", D_CIV),
    ("P22-ET-06-007-001", "-", "Especificación técnica de montaje electromecánico", "0", D_ETM),
    ("P22-ET-06-007-002", "-", "Especificación técnica de montaje de cañerías HDPE", "0", D_ETM),
    ("PLANO MONOGRAFIA TALTAL", "única", "Plano de monografía del levantamiento del sitio, abril de 2026", "-", D_SIT),
    ("DES TALTAL_transparent_mosaic", "-", "Ortomosaico del levantamiento del sitio, abril de 2026", "-", D_SIT),
    ("EX-26005-F01", "única", "Plano de fabricación del estanque de salmuera TK-06-001, Exfibro", "0", D_EQU),
    ("KSB-AAF-KNCPP11-050+160M", "única", "Plano de arreglo general de la bomba de alimentación BH-06-001, KSB", "A", D_EQU),
    ("DWG-1206D", "única", "Plano de la válvula de retención de doble placa de 4 pulgadas, VR-06-001 y VR-06-003, VATAC para KSB", "01", D_EQU),
    ("ISORIA 10", "-", "Folleto de la serie de las válvulas mariposa VM-06, con dimensiones y pesos, KSB", "-", D_EQU),
    ("MS_MC", "-", "Folleto del reductor manual MS/MC de las válvulas mariposa, KSB", "-", D_EQU),
    ("ALS200", "-", "Folleto del final de carrera ALS 200 de las válvulas mariposa, KSB", "-", D_EQU),
]


# ------------------------------------------------------- gate de sincronizacion
def _rev_del_nombre(stem, codigo):
    """Revision declarada en el nombre del archivo, o None si no la trae.

    Convenciones que conviven en el paquete:
      P22-DWG-06-006-005-2 (...)      -> 2   (mecanica, guion)
      P22-DWG-00-002-002_1 LAM1       -> 1   (civil, guion bajo)
      P22-ET-00-010-101-0_1           -> 1   (ET civil, correlativo mas revision)
      P22-DWG-06-006-010 (...)        -> None (sin sufijo de revision)
      EX-26005-F01-Rev0               -> 0   (proveedor, prefijo Rev)
      KSB-AAF-KNCPP11-050+160M_A      -> A   (proveedor, revision de una letra)
      DWG-1206D-RV01                  -> 01  (proveedor, prefijo RV)
    Se toma el ultimo token de revision anterior al primer espacio o parentesis.
    """
    resto = stem[len(codigo):]
    resto = re.split(r"[ (]", resto, maxsplit=1)[0]
    tokens = re.findall(r"[-_](?:Rev|RV)?(\d+|[A-Z])(?![A-Za-z])", resto)
    return tokens[-1] if tokens else None


def _laminas_declaradas(texto):
    """Expande 'LAM2 y LAM3', 'H.1 a H.5' o 'LAM1' a la lista de marcas a buscar."""
    marcas = re.findall(r"LAM\s?\d+", texto)
    if marcas:
        return [m.replace(" ", "") for m in marcas]
    hojas = re.findall(r"H\.(\d+)", texto)
    if len(hojas) == 2 and " a " in texto:
        return [f"H.{n}" for n in range(int(hojas[0]), int(hojas[1]) + 1)]
    if hojas:
        return [f"H.{n}" for n in hojas]
    return []


def comprobar_vigencia_contra_paquete(tolerar_faltantes=False):
    """Aborta si la hoja Vigencia no describe el arbol real del paquete."""
    if not PAQUETE.is_dir():
        sys.exit(f"ERROR: no existe el paquete en {PAQUETE}")

    archivos = [p for p in PAQUETE.rglob("*")
                if p.is_file() and not p.name.startswith(".")
                and p.suffix.lower() in {".pdf", ".xlsx", ".docx", ".nwd", ".dwg", ".tif"}]

    errores = []
    for codigo, lamina, titulo, rev, _dossier in VIGENCIA:
        if rev == "-":                                   # el modelo 3D no lleva revision
            if not any(codigo in p.name for p in archivos):
                errores.append(f"{codigo}: sin archivo en el paquete")
            continue

        candidatos = [p for p in archivos if p.stem.startswith(codigo)]
        if not candidatos:
            errores.append(f"{codigo} {lamina}: sin archivo en el paquete")
            continue

        marcas = _laminas_declaradas(lamina)
        grupos = [[p for p in candidatos if m in p.stem.replace(" ", "")] for m in marcas] \
            if marcas else [candidatos]

        for marca, grupo in zip(marcas or ["-"], grupos):
            if not grupo:
                errores.append(f"{codigo} {marca}: declarada pero sin archivo")
                continue
            revs = {_rev_del_nombre(p.stem, codigo) for p in grupo}
            if rev == "sin sufijo de revision":
                if revs != {None}:
                    errores.append(f"{codigo} {marca}: se declara sin sufijo y el archivo trae {revs}")
            elif revs != {rev}:
                errores.append(
                    f"{codigo} {marca}: se declara revision {rev} y el paquete tiene {sorted(str(r) for r in revs)}")

    declarados = {c for c, *_ in VIGENCIA}
    for p in archivos:
        if p.parent.name == "anexos" or "0. CONTROL DE CAMBIOS" in str(p) or p.name == INDICE:
            continue
        if not any(p.stem.startswith(c) or c in p.name for c in declarados):
            errores.append(f"{p.name}: en el paquete y no declarado en la hoja Vigencia")

    if tolerar_faltantes:
        faltantes = [e for e in errores if e.endswith("sin archivo en el paquete")]
        errores = [e for e in errores if e not in faltantes]
        if faltantes:
            print(f"    {len(faltantes)} documentos declarados sin archivo en este equipo "
                  f"(arbol a medio sincronizar); se dejan pasar por --arbol-incompleto:")
            for e in faltantes:
                print("      -", e)

    if errores:
        print("La hoja Vigencia no coincide con el paquete:")
        for e in errores:
            print("  -", e)
        sys.exit(1)
    print(f"    Vigencia contrastada contra el paquete: {len(VIGENCIA)} documentos, sin diferencias.")


# --------------------------------------------------------------------------- helpers
def encabezado(ws, fila, titulos, anchos):
    for j, (t, a) in enumerate(zip(titulos, anchos), start=1):
        c = ws.cell(row=fila, column=j, value=t)
        c.font = Font(name=FUENTE, size=10, bold=True, color="FFFFFFFF")
        c.fill = AZUL
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDE
        ws.column_dimensions[get_column_letter(j)].width = a
    ws.row_dimensions[fila].height = 30
    ws.freeze_panes = ws.cell(row=fila + 1, column=1)


def fila_datos(ws, fila, valores, resaltar=False):
    for j, v in enumerate(valores, start=1):
        c = ws.cell(row=fila, column=j, value=v)
        c.font = Font(name=FUENTE, size=9)
        c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c.border = BORDE
        if resaltar:
            c.fill = AMAR
        if isinstance(v, (int, float)):
            c.alignment = Alignment(horizontal="center", vertical="top")
            c.number_format = "#,##0.00" if isinstance(v, float) else "#,##0"


def titulo_hoja(ws, texto, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=texto)
    c.font = Font(name=FUENTE, size=12, bold=True)
    c.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 22


# --------------------------------------------------------------------------- hojas
def hoja_resumen(wb):
    ws = wb.active
    ws.title = "Resumen"
    titulo_hoja(ws, "Ingenieria vigente para construccion: que rige y que cambio", 4)
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 62
    filas = [
        ("Paquete", "INGENIERIA VIGENTE PARA CONSTRUCCION, montaje mecanico y obras civiles"),
        ("Fecha", "14-09-2026"),
        ("Destinatario", "Contratista adjudicado. El contrato esta adjudicado y este paquete no reabre la licitacion."),
        ("Que rige", "Para cada codigo y lamina rige la revision que este paquete entrega, listada en la hoja Vigencia. Cualquier revision anterior del mismo documento queda reemplazada."),
        ("Que NO reemplaza", "Las Bases de Licitacion ni el Formato de Presupuesto, que son contractuales y no se reemiten. Este paquete lleva solo ingenieria."),
        ("", ""),
        ("Cambio de fondo", "La fundacion del contenedor del modulo sube 250 mm de cota, de la +6,050 a la +6,300, y con ella suben las cuatro cotas de conexion con el modulo. Los tie-ins con el modulo existente no cambian."),
        ("", ""),
        ("Documentos del paquete", 63),
        ("Documentos mecanicos que cambian de revision", 12),
        ("Laminas civiles que cambian de revision", 8),
        ("Partidas de obra civil que cambian de cantidad", 2),
        ("Isometrias sin cambio alguno respecto de la revision cotizada", "7 de 11 (identicas byte a byte)"),
        ("Archivos del paquete", 88),
        ("", ""),
        ("La cubierta del sistema CIP no se construye", "El Formato de Presupuesto cotiza su fundacion en la partida 4.3 Fundacion de la cubierta metalica del sistema CIP (cobertizo), que se ejecuta integra con los 24 pernos F-1554 de 3/4 de pulgada colados y su proteccion anticorrosiva interina. La estructura metalica no tiene partida en el Formato y la ejecuta ADASA en una etapa posterior."),
        ("Numeracion de las partidas", "Se cita la del Formato de Presupuesto contractual. Ese Formato repite dos codigos, 4.3 y 4.7, por lo que cada partida va con su numero y su nombre completo."),
        ("La brida no cambia de tipo", "En las dos revisiones es la misma pieza: flange suelto de junta solapada sobre stub end (LJ = Lap Joint), con perforaciones ASME B16.5 clase 150. La revision 1 del listado incorpora su material, acero galvanizado por inmersion, que las isometrias no declaran. Para el material rige el listado."),
        ("Que revisar con atencion", "Las cuatro cotas de conexion con el modulo, la fundacion del sistema CIP, y el listado de materiales, que cambia accesoria y material de brida sin cambiar los metros de cañeria."),
    ]
    r = 3
    for a, b in filas:
        ca = ws.cell(row=r, column=1, value=a)
        ca.font = Font(name=FUENTE, size=10, bold=bool(a))
        ca.alignment = Alignment(vertical="top")
        cb = ws.cell(row=r, column=2, value=b)
        cb.font = Font(name=FUENTE, size=10)
        cb.alignment = Alignment(vertical="top", wrap_text=True)
        if isinstance(b, int):
            cb.alignment = Alignment(horizontal="left", vertical="top")
            cb.number_format = "#,##0"
        if a and not isinstance(b, int):
            ws.row_dimensions[r].height = 34
        r += 1


def hoja_tabla(wb, nombre, titulo, cabeceras, anchos, datos, resaltar_si=None):
    ws = wb.create_sheet(nombre)
    titulo_hoja(ws, titulo, len(cabeceras))
    encabezado(ws, 3, cabeceras, anchos)
    for i, d in enumerate(datos, start=4):
        fila_datos(ws, i, d, resaltar=bool(resaltar_si and resaltar_si(d)))
        ws.row_dimensions[i].height = 46
    return ws


def main():
    # El gate contrasta la hoja Vigencia contra el arbol real y aborta ante cualquier
    # diferencia. Con --arbol-incompleto se deja pasar SOLO la falta de archivos, que en
    # un equipo con Synology a medio sincronizar no es un defecto del paquete. Toda otra
    # diferencia sigue abortando, y la planilla queda marcada como provisoria: hay que
    # regenerarla sin el flag antes de entregarla.
    incompleto = "--arbol-incompleto" in sys.argv
    comprobar_vigencia_contra_paquete(tolerar_faltantes=incompleto)
    if incompleto:
        print("AVISO: planilla generada con --arbol-incompleto. NO se entrega asi.")

    wb = Workbook()
    hoja_resumen(wb)

    hoja_tabla(wb, "Vigencia", "Revision que rige para cada documento del paquete",
               ["Codigo", "Lamina u hoja", "Titulo", "Revision vigente", "Dossier"],
               [24, 18, 58, 16, 26], VIGENCIA)

    hoja_tabla(wb, "Mecanica", "Ingenieria de detalle mecanica: documentos que cambian respecto de la revision cotizada",
               ["Codigo", "Lamina u hoja", "Titulo", "Revision cotizada", "Revision vigente",
                "Origen", "Que cambio", "Afecta a lo cotizado", "Partida de obra civil"],
               [22, 12, 34, 14, 14, 26, 74, 12, 26], MECANICA,
               resaltar_si=lambda d: d[7] == "Si")

    hoja_tabla(wb, "Civil", "Ingenieria de detalle de obras civiles: laminas que cambian respecto de la revision cotizada",
               ["Codigo", "Lamina", "Titulo", "Revision cotizada", "Revision vigente",
                "Origen", "Que cambio", "Afecta a lo cotizado", "Partida del Formato"],
               [22, 10, 34, 14, 14, 26, 74, 12, 40], CIVIL_CAMBIA,
               resaltar_si=lambda d: d[7] == "Si")

    ws = hoja_tabla(wb, "Cubicaciones",
                    "Obras civiles: cantidades cotizadas contra cantidades de la ingenieria vigente",
                    ["Partida", "Nombre de la partida en el Formato", "Unidad",
                     "Cantidad cotizada", "Cantidad vigente", "Diferencia", "Respaldo"],
                    [9, 52, 9, 17, 17, 12, 46],
                    [(a, b, u, q0, q1, round(q1 - q0, 2), src) for a, b, u, q0, q1, src in CUBICACIONES],
                    resaltar_si=lambda d: d[5] != 0)
    for i in range(4, 4 + len(CUBICACIONES)):
        ws.row_dimensions[i].height = 18
    r = 4 + len(CUBICACIONES) + 1
    c = ws.cell(row=r, column=1,
                value="Las partidas por unidad de obra se pagan segun la cubicacion realmente ejecutada. "
                      "El Formato repite los codigos 4.3 y 4.7, por lo que cada partida se cita con su nombre completo.")
    c.font = Font(name=FUENTE, size=9, italic=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)

    for hoja in wb.worksheets:
        hoja.sheet_view.showGridLines = False
    wb.save(SALIDA)
    print(f"OK: {SALIDA.name}")
    print(f"    Vigencia {len(VIGENCIA)} | Mecanica {len(MECANICA)} | Civil {len(CIVIL_CAMBIA)} "
          f"| Cubicaciones {len(CUBICACIONES)}")


if __name__ == "__main__":
    main()
