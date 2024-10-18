"""
___________________________________________________________________________________________________

  LGA_UTF-pyCleaner v1.2 | 2024 | Lega  
  Tool for removing accents and the letter 'ñ' from .py files in the specified directory.
  Processes all .py files in the given directory, including subdirectories.
___________________________________________________________________________________________________

"""


import os
import sys
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

def main():
    if len(sys.argv) > 1:
        base_directory = sys.argv[1]
        if not os.path.isdir(base_directory):
            print(f"La ruta proporcionada no es una carpeta válida: {base_directory}")
            sys.exit(1)
    else:
        base_directory = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Procesando directorio: {base_directory}")
    process_directory(base_directory)
    print("Proceso completado.")

if __name__ == "__main__":
    main()
