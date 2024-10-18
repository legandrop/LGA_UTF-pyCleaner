"""
___________________________________________________________________________________________________

  LGA_UTF-Cleaner v1.2 | 2024 | Lega  
  Tool for removing accents and the letter 'ñ' from .py files in the script's directory.
  Processes all .py files in the directory where the script is located, including subdirectories.
___________________________________________________________________________________________________

"""


import os
import unicodedata

def remove_accents(input_str):
    # Transformar la cadena a unicode normalizado
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Eliminar acentos y reemplazar ñ por n
    new_content = remove_accents(content).replace('ñ', 'n').replace('Ñ', 'N')

    # Solo sobrescribir si hubo cambios
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Archivo modificado: {file_path}")
        print_changes(content, new_content)
    else:
        print(f"No se requirieron cambios en: {file_path}")

def print_changes(old_content, new_content):
    old_lines = old_content.splitlines()
    new_lines = new_content.splitlines()
    
    for i, (old_line, new_line) in enumerate(zip(old_lines, new_lines)):
        if old_line != new_line:
            print(f"  Línea {i+1}:")
            print(f"    Antes: {old_line}")
            print(f"    Después: {new_line}")
            print()

def process_directory(directory):
    script_name = os.path.basename(__file__)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and file != script_name:
                file_path = os.path.join(root, file)
                process_file(file_path)

# Obtener el directorio donde se encuentra el script
script_directory = os.path.dirname(os.path.abspath(__file__))
print(f"Procesando archivos en: {script_directory}")
process_directory(script_directory)
print("Proceso completado.")
