# Hicimos esta clase para generar un informe con el resultado del procesamiento de las imagenes
class ReportGenerator:
    def __init__(self):
        self.success = []
        self.fail = []

# REcibimos los dos diccionarios y los convertimos en listas
    def generate_report(self, success_dict, fail_dict):
        self.success = [{"image": image, "status": status} for image, status in success_dict.items()]
        self.fail = [{"image": image, "status": status} for image, status in fail_dict.items()]
# Convertimos cada entrada a un diccionario por elemento, para poder visualizarlo más fácil después.
        return {
            "success": self.success,
            "fail": self.fail
        }

    def print_report(self, verbose=False):
        if verbose:
            print("\nImágenes Procesadas con Éxito:")
            for item in self.success:
                print(f"Imagen: {item['image']} - Estado: {item['status']}")

            print("\nImágenes que Fallaron:")
            for item in self.fail:
                print(f"Imagen: {item['image']} - Estado: {item['status']}")
# Los print eran para visualizar las listas que contenian, después los omití con verbose.