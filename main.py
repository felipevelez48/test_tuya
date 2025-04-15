from source.file_finder import FileFinder
from source.image_encoder import ImageEncoder
from source.html_processor import HTMLProcessor
from pathlib import Path

if __name__ == "__main__":
    source_directory = "samples"
    output_directory = "output"

    finder = FileFinder(source_directory)
    html_files = finder.find_html_files()
    encoder = ImageEncoder()
    processor = HTMLProcessor(encoder)

    total_success = 0
    total_fail = 0

    print("--- Archivos HTML encontrados por FileFinder ---")
    if html_files:
        for file_p in html_files:
            print(f"- {file_p}")
    else:
        print("Ninguno.")
    print("----------------------------------------------\n")

    for html_file in html_files:
        print(f"Procesando: {html_file}")
        report = processor.process_file(str(html_file), output_directory)

        success_count = len(report["success"])
        fail_count = len(report["fail"])
        total_success += success_count
        total_fail += fail_count

        print(f"✔ Imágenes convertidas: {success_count}")
        print(f"✘ Imágenes fallidas: {fail_count}")
        print("-" * 40)

    total = total_success + total_fail
    print("\nResumen final:")
    print(f"🔍 Total de imágenes encontradas: {total}")
    print(f"✔ Total convertidas: {total_success}")
    print(f"✘ Total fallidas: {total_fail}")

