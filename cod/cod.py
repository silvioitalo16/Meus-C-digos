estoque = []

while True: 
    opcao = int(input('1 - Cadastrar; 2 - Total Finaceiro; 3 - Quantidades; 4 - Sair '))
    if opcao == 1:
        produto = {}
        produto['nome'] = input('Nome do produto: ')
        produto['preco'] = float(input('Preco do produto: '))
        produto['qtd'] = float(input('Quantidade do produto: '))
        estoque.append(produto)
        print(estoque)

    if opcao == 2:
        idx = int(input('Indice do produto: '))
        produto = estoque[idx]
        preco = produto['preco']
        qtd = produto['qtd']
        print('Total: ', preco * qtd)

    if opcao == 3:
        for produto in estoque:
            print(produto['nome'], '-', produto['qtd'])

    if opcao == 4:

        break                    
    
    