import cv2 as cv

cap = cv.VideoCapture(0)
frameEstatua = None

while True:
   
    ret, frame = cap.read()

    cv.imshow('Original', frame)

    if cv.waitKey(1) & 0xFF == ord('e'):
        frameEstatua = frame.copy()
        print("Frame capturado!")

    if cv.waitKey(1) & 0xFF == ord('s'):
        break

    if frameEstatua is not None:
        frame_diff = cv.absdiff(frameEstatua, frame)

        gray_diff = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)#cinza

        _, threshold_diff = cv.threshold(gray_diff, 40, 255, cv.THRESH_BINARY)#binarizar

        cv.imshow('Subtracao Binarizada', threshold_diff)#resultadodabinarização

cap.release()
cv.destroyAllWindows()
