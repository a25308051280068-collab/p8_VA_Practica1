import cv2
print("Christian Garcia Jimenez Nc = 0068")
# Cargar la imagen
imagen = cv2.imread("canguro.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada_0068 = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original 0068 Christian G", imagen)
cv2.imshow("Imagen con filtro de mediana 0068 Christian G", imagen_filtrada_0068)

# Guardar resultado
cv2.imwrite(
    "canguro.jpg Nc = 0068",
    imagen_filtrada_0068
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("canguro.jpg Nc = 0068")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Christian Garcia Jimenez Nc = 0068")
