import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)


while True:
    capturou, frame = webcam.read()
   
    b,g,r = cv.split(frame)
    be = cv.equalizeHist(b)
    ge = cv.equalizeHist(g)
    re = cv.equalizeHist(r)
    img = cv.merge((be, ge, re))

    cv.imshow('original',frame)
    cv.imshow('equalizada',img)
    tecla = cv.waitKey(1) # precionar "s" para fechar
    if ord('s') == tecla:
        break


#mostra a webcam em tempo real equalizada

