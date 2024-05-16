import cv2 as cv


def agucar_imagem(imagem, nivel):
   
    imagem_embacada = cv.blur(imagem, (10,10))
    diff = cv.subtract(imagem,imagem_embacada)
    return cv.add(imagem, diff * nivel)
   
cap = cv.VideoCapture(0)

nivel_agucamento = 0

while True:
    ret, frame = cap.read()
    cv.imshow('immagem', agucar_imagem(frame,nivel_agucamento))
   

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        nivel_agucamento = 0
    elif key == ord('w'):
        nivel_agucamento = 1
    elif key == ord('e'):
        nivel_agucamento = 2
    elif key == ord('r'):
        nivel_agucamento = 3
    elif key == ord('s'):
        break

