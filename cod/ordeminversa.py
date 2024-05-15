def mostrar_ordem_inversa(vetor):
    vetor.reverse()  
    for numero in vetor:
        print(numero)
numeros_reais = []
print("Insira 10 números reais:")
for _ in range(10):
    numero = float(input())
    numeros_reais.append(numero)

mostrar_ordem_inversa(numeros_reais)