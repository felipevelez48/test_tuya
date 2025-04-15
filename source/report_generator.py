class ReportGenerator:
    def __init__(self):
        self.success = []
        self.fail = []

# REcibimos los dos diccionarios y los convertimos en listas
    def generate_report(self, success_dict, fail_dict):
        self.success = [{"image": image, "status": status} for image, status in success_dict.items()]
        self.fail = [{"image": image, "status": status} for image, status in fail_dict.items()]

        return {
            "success": self.success,
            "fail": self.fail
        }

    def print_report(self):
        print("\nImágenes Procesadas con Éxito:")
        for item in self.success:
            print(f"Imagen: {item['image']} - Estado: {item['status']}")

        print("\nImágenes que Fallaron:")
        for item in self.fail:
            print(f"Imagen: {item['image']} - Estado: {item['status']}")
