import cv2 as cv

import numpy as np

img = cv.imreadimagem = cv.imread('imagem', 0)

limite_inferior = 100
limite_superior = 200

img_clipe = np.clip(img, limite_inferior, limite_superior)

cv.imshow('Resultado', img_clipe)
cv.waitKey(0)
cv.destroyAllWindows()