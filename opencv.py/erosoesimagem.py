import cv2 as cv

img = cv.imread('fit.jpg',cv.IMREAD_GRAYSCALE)
original = img.copy()
qtd = int(input('Digite a quantidade de erosoes:'))

kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
for i in range(qtd):

    img = cv.erode(img,kernel)

   
cv.imshow('img',original)
cv.imshow('res',img)

cv.waitKey(0)
