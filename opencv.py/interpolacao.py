import cv2 as cv

img = cv.imread('moon.jpg')

for fator in range(1,101):
    reduzida = cv.resize(img,None,fx=1/fator,fy=1/fator)
    res = cv.resize(reduzida,None,fx=fator,fy=fator,interpolation=cv.INTER_NEAREST)
   
     
   
cv.imshow('resduzida',reduzida)
cv.imshow('resultado',res)
   
   
cv.waitKey(0)