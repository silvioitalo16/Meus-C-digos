litros = float(input('digite a quantidade de litros:'))
tipo = input('tipo do combustivel:')

precoAlcool = 5.6
precoGasolina = 6.5

if tipo == 'A':

    if litros <= 20:

        total = precoAlcool * litros * 0.97
  
    else:

        total = precoAlcool * litros * 0.95

elif tipo == 'G':

    if litros <= 20:

        total = precoGasolina * litros * 0.95

    else:

        total = precoGasolina * litros * 0.94

else:

    total = 0

 

print ('total: R$', total)