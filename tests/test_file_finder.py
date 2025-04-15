from source.file_finder import FileFinder

finder = FileFinder("samples")
archivos = finder.find_html_files()
print(archivos)
