# Creamos este archivo para que actuara como el orquestador de los demás, dándole paárametos.
from source.file_finder import FileFinder
from source.image_encoder import ImageEncoder
from source.html_processor import HTMLProcessor
from pathlib import Path

# Importamos los módulos de los demás archivos
# Definimos ruta de entrada y salida, he inicializamos los demás archivos.
if __name__ == "__main__":
    source_directory = "samples"
    output_directory = "output"

    finder = FileFinder(source_directory)
    html_files = finder.find_html_files()
    encoder = ImageEncoder()
    processor = HTMLProcessor(encoder)

    total_success = 0
    total_fail = 0
    file_success_map = {}  # Para saber cuántas imágenes fueron convertidas por archivo

# Hacemos una lista de los archivos encontrados por FileFinder
    print("\n--- Archivos HTML encontrados por FileFinder ---")
    if html_files:
        for file_p in html_files:
            print(f"- {file_p}")
    else:
        print("Ninguno.")
    print("----------------------------------------------\n")

    print("Procesando archivos...\n")

    for html_file in html_files:
        report = processor.process_file(str(html_file), output_directory)

        success_count = len(report["success"])
        fail_count = len(report["fail"])
        total_success += success_count
        total_fail += fail_count

        # Guardamos el nombre del archivo y la cantidad de imágenes convertidas
        file_success_map[Path(html_file).name] = success_count

    total = total_success + total_fail

    # Mostramos el resumen final, de acuerdo a los parámetros del ehjercicio
    print("\n✅ Resumen final:")
    print(f"- Archivos procesados: {len(html_files)}")
    print(f"- Total imágenes encontradas: {total}")
    print(f"- ✔ Total convertidas: {total_success}")
    print(f"- ✘ Total fallidas: {total_fail}")
# Acá damos resumen de acuerdo a los archivos .html a cuales pertenecen cada una de las imagenes convertidas.
    print("\nImágenes convertidas por archivo:")
    for filename, count in file_success_map.items():
        print(f"- {filename}: {count}")

