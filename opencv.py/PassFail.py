import cv2 as cv
import numpy as np


texto = "Fail"  # "Fail" ou "Pass" 

if texto == "Pass":
    cor = (0, 255, 0)  # Verde para "Pass"
else:
    cor = (0, 0, 255)  # Vermelho para "Fail"

# imagem em branco
imagem = 255 * np.ones((300, 300, 3), dtype="uint8")

# Desenho do retângulo na imagem
cv.rectangle(imagem, (50, 50), (250, 250), cor, -1)

# imagem com o retangulo
cv.imshow('Resultado', imagem)
cv.waitKey(0)
cv.destroyAllWindows()