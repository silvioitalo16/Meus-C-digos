import cv2 as cv

fit = cv.imread('fit.jpg')
robot = cv.imread('robot.jpg')

fitGray = cv.cvtColor(fit,cv.COLOR_BGR2GRAY)
_, fitBin = cv.threshold(fitGray,230,255,cv.THRESH_BINARY)
fitMask = cv.cvtColor(fitBin,cv.COLOR_GRAY2BGR)

robotAndMask = cv.bitwise_and(fitMask,robot)

fitMaskInv = cv.bitwise_not(fitMask)
fitAndMaskInv = cv.bitwise_and(fitMaskInv,fit)

resultado = cv.bitwise_or(fitAndMaskInv,robotAndMask)

cv.imshow('mascara',fitMask)
cv.imshow('mascarainv',fitMaskInv)
cv.imshow('intermediario1',robotAndMask)
cv.imshow('intermediario2',fitAndMaskInv)
cv.imshow('resultado',resultado)
cv.waitKey(0)