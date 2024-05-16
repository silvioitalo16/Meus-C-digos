import cv2 as cv
import numpy as np

imagem = cv.imread('img', 0)  

bordas1 = cv.Canny(imagem, 50, 200)
 
cv.imshow('Bordas1', bordas1)

cv.waitKey(0)
