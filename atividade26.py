compras = []

while True:
    print('Escolha uma opção:')
    print('1 - Adicionar item')
    print('2 - Exibir lista')
    print('3 - Remover item')
    print('4 - Finalizar')

    opcao = input('Digite o número da opção: ')

    if opcao == '1':
        item = input('Digite o nome do item para adicionar: ')
        compras.append(item)
        print(f'Item "{item}" adicionado à lista.')
        
    elif opcao == '2':
        if compras:
            print(f'{item}')
        else:
            print('A lista está vazia.')
            
    elif opcao == '3':
        item = input('Digite o nome do item que deseja remover: ')
        if item in compras:
            compras.remove(item)
            print(f'Item {item} removido.')
        else:
            print('Item não encontrado.')

    elif opcao == '4':
        print(f'{compras}')
        print('Programa finalizado.')
        break

    else:
        print('ESCOLHA DE 1 A 4')  
