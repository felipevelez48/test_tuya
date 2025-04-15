from image_encoder import ImageEncoder  # si estás dentro de source
# o bien: from source.image_encoder import ImageEncoder  # si estás en raíz

encoder = ImageEncoder()
base64_string = encoder.encode_image("../images/tuya.png")

if base64_string:
    print("✅ Codificación exitosa!")
    print(base64_string[:100] + "...")  # solo imprime los primeros 100 caracteres
else:
    print("❌ Algo salió mal...")
