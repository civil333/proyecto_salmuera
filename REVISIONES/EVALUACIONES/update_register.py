import os
import re
import pandas as pd
import glob

# Rutas de trabajo
base_dir = r"c:\SynologyDrive\SynologyDrive\DESAROLLO PROYECTOS CLAUDE\MODULO DE SALMUERA TALTAL\REVISIONES"
transmittals_dir = os.path.join(base_dir, "TRANSMITTALES")
evaluations_dir = os.path.join(base_dir, "EVALUACIONES")
excel_file = os.path.join(evaluations_dir, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
output_file = os.path.join(evaluations_dir, "P22-IT-06-000-002-2_Master-Deliverable-Register.xlsx")

def extract_updates_from_md(md_path, tm_name):
    """Extrae las lineas de tabla del archivo markdown que coincidan con un patron de documento."""
    updates = {}
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        # Buscamos lineas que parezcan filas de tabla conteniendo "P22-"
        # Ejemplo: | 1 | P22-ET-09-000-01 | DS Container | comentarios | **4 - Rejected** |
        for line in f:
            if "|" in line and "P22-" in line:
                cols = [c.strip() for c in line.split("|")]
                if len(cols) > 3:
                    # Encontrar la columna del codigo del documento
                    doc_code = None
                    for col in cols:
                        if re.match(r"P22-[A-Z]+-09-[\d-]+", col):
                            doc_code = col
                            break
                    
                    if doc_code:
                        # Asumimos que el veredicto esta en la ultima y los comentarios/acciones en la penultima
                        verdict = cols[-2].replace('**', '').strip() if len(cols) > 2 else ""
                        comments = cols[-3].strip() if len(cols) > 3 else ""
                        
                        # Limpiar veredicto
                        if "Approved as noted" in verdict or "2 -" in verdict or "2-" in verdict:
                            clean_verdict = "2-AN"
                        elif "Approved" in verdict or "1 -" in verdict or "1-" in verdict:
                            clean_verdict = "1-Approved"
                        elif "Rejected" in verdict or "4 -" in verdict or "4-" in verdict:
                            clean_verdict = "4-Rejected"
                        elif "To be revised" in verdict or "3 -" in verdict or "3-" in verdict:
                            clean_verdict = "3-TBR"
                        else:
                            clean_verdict = verdict
                            
                        # Limpiar TM format
                        tm_num = tm_name.split("-")[3] if "P22-TM-" in tm_name else tm_name
                        tm_str = f"N{int(tm_num)}" if tm_num.isdigit() else tm_name
                        
                        updates[doc_code] = {
                            "Verdict": clean_verdict,
                            "TM": tm_str,
                            "Action Required": comments
                        }
    return updates

print("Iniciando actualizacion de Master Register (Proceso AI Luis)...")

# 1. Leer todas las carpetas de Transmittales
all_updates = {}
for root, dirs, files in os.walk(transmittals_dir):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)
            folder_name = os.path.basename(root)
            dict_updates = extract_updates_from_md(md_path, folder_name)
            
            # Combinamos las actualizaciones temporalmente (esto pisara las más antiguas si hay conflicto en el mismo script)
            # En un entorno real, dependeria de un orden cronologico, pero confiaremos en que el arbol os.walk
            # o los transmittals con numeros mayores pisen a iteraciones previas
            
            for code, data in dict_updates.items():
                all_updates[code] = data

print(f"Se encontraron actualizaciones para {len(all_updates)} documentos.")

# 2. Cargar Excel Original
try:
    df = pd.read_excel(excel_file)
    print("Excel original cargado correctamente.")
    
    # 3. Aplicar actualizaciones
    updated_count = 0
    for idx, row in df.iterrows():
        code = str(row['Code / ET Reference']).strip()
        if code in all_updates:
            df.at[idx, 'Verdict'] = all_updates[code]["Verdict"]
            df.at[idx, 'TM'] = all_updates[code]["TM"]
            # df.at[idx, 'Action Required'] = all_updates[code]["Action Required"] # Opcional si queremos traer los comments
            updated_count += 1
# Removed print statement to avoid encoding error

    # 4. Guardar archivo Version 2
    df.to_excel(output_file, index=False)
    print(f"Archivo version 2 guardado en: {output_file}")
    print(f"Total documentos actualizados en el Excel: {updated_count}")
    
except Exception as e:
    print(f"Error procesando el archivo excel: {e}")
