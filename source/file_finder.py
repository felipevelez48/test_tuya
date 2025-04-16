# Definimos está clase para buscar los archivos de acuerdo a una ruta relativa dada en el archivo ejecutable main.py
from pathlib import Path
from typing import List, Union

# Creamos la clase Filefinder para buscar los archivos cuyo sufijo termine en .html
class FileFinder:
    def __init__(self, input_path: Union[str, Path]):
        self.input_path = Path(input_path)
# Convierte el input_path en un objeto y lo guardamos como atributo.

# Nos devuelve la lista de archivos .html encontrados.
    def find_html_files(self) -> List[Path]:
        if self.input_path.is_file() and self.input_path.suffix == ".html":
            return [self.input_path]
        elif self.input_path.is_dir():
            return list(self.input_path.rglob("*.html"))
# Validamos si la ruta es un archivo o si la ruta es un directorio y nos devuelve la lista con los que encuentre.
        else:
            return []
# En caso de no encontrar nada, nos devulve una lista vacía.
