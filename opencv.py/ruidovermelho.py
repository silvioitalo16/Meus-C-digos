import cv2 as cv

img = cv.imread('celularRuido.jpg')

res = cv.medianBlur(img, 5)

cv.imshow('imagem original',img)
cv.imshow('Resultado',res)

cv.waitKey(0)

#codigo abre a imagem e elimina os ruidos vermelhos da imagem