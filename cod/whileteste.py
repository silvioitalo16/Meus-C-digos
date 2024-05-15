while True:

    nota = float(input("Informe a nota : "))

    if 0 <= nota <= 10:

        print("Nota válida!")

        break

    else:

        print("Nota inválida.Por favor, informe a nota novamente.")