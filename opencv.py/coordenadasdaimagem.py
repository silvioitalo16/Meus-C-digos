import cv2 as cv

imagem = cv.imread('fit.jpg')

x = 100
y = 50

altura, largura, canais = imagem.shape
if x >= largura or y >= altura:
    print("Coordenadas inválidas")
else:
    (azul, verde, vermelho) = imagem[y, x]
    print("Canal Azul:", azul)
    print("Canal Verde:", verde)
    print("Canal Vermelho:", vermelho)