import cv2 as cv 

# Carrega os classificadores em cascata para rostos e olhos
rostos_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
olhos_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

# Inicia a webcam
webcam = cv.VideoCapture(0)

while True:
    # Captura a webcam
    retorno, frame = webcam.read()
    if not retorno:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detecta os rostos
    faces = rostos_cascade.detectMultiScale(gray, 1.3, 5)

    # Para cada rosto encontrado, desenhar um retângulo ao redor do rosto e detectar olhos
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = olhos_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # frame com os rostos e olhos detectados
    cv.imshow('Deteccao de Rostos e Olhos', frame)

    # pressionar a tecla 'q' para fechar as janelas
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()