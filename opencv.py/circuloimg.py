import cv2 as cv

from numpy import sqrt, pi

img = cv.imread('imagem')
x = int(input('coordenada x :'))
y = int(input('coordenada y :'))
area = float(input('area do circulo:'))
raio = int(sqrt(area/pi))

res = cv.circle(img.copy(),(x,y),raio,(255,0,0),-1)

cv.imshow('img',img)
cv.imshow('res',res)
cv.waitKey(0)

#desenhar um circulo na imagem