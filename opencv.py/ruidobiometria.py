import cv2 as cv

img = cv.imread('biometria.JPG',cv.IMREAD_GRAYSCALE)

Kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
res = cv.morphologyEx(img,cv.MORPH_CLOSE,Kernel)
Kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(7,7))
res = cv.morphologyEx(res,cv.MORPH_OPEN,Kernel)



cv.imshow('img',img)
cv.imshow('res',res)

cv.waitKey(0)

