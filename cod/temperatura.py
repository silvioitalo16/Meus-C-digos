temperaturas = []
while True:
    temperatura = float(input("Digite a temperatura (digite 100 para parar): "))
    if temperatura == 100:
        break
    temperaturas.append(temperatura)

if temperaturas:
    menor_temperatura = min(temperaturas)
    maior_temperatura = max(temperaturas)
    media_temperatura = sum(temperaturas) / len(temperaturas)
    print(f"A menor temperatura é {menor_temperatura}°C")
    print(f"A maior temperatura é {maior_temperatura}°C")
    print(f"A média das temperaturas é {media_temperatura}°C")
else:
    print("Nenhuma temperatura foi inserida.")