import cv2 as cv 
import numpy as np

img = cv.imread('imagem')
vermelho = np.array([0, 0, 255])

coordenadas = np.argwhere(np.all(img == vermelho, axis=-1))

if len(coordenadas) > 0:
    for coord in coordenadas:
        print("Coordenadas do pixel vermelho:", coord)
else:
    print("Sem vermelho")