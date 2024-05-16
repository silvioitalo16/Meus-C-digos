import cv2 as cv

imagem = cv.imread('imagem')

x1, y1 = 500, 50
x2, y2 = 200, 250

cv.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), -1)

cv.imshow('Imagem pintada', imagem)
cv.waitKey(0)
cv.destroyAllWindows()