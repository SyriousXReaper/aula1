estoque = {}

while True:
    print('Escolha uma opção:')
    print('1 - Adicionar item')
    print('2 - Pesquisar item')
    print('3 - Atualizar item')
    print('4 - Finalizar')
    
    opcao = input('Digite o número da opção: ')
    
    if opcao == '1':
        item = input('Digite um item para adicionar: ')
        n_item = int(input('Digite a quantidade desse item: '))
        estoque[item] = n_item
        print(f'Item {item} adicionado com {n_item} unidades.')
        
    elif opcao == '2':
        item = input('Digite o nome do item para pesquisar: ')
        if item in estoque:
            print(f'O item {item} tem {n_item} unidades em estoque.')
        else:
            print(f'O item não encontrado.')
            
    elif opcao == '3':
        item = input('Digite o nome do item que deseja atualizar: ')
        if item in estoque:
            n_item2 = int(input('Digite a nova quantidade: '))
            estoque[item] = n_item2
            n_item = n_item2
            print(f"Atualizado {item} {n_item2}")
        else:
            print('Item não encontrado no estoque.')

    elif opcao == '4':
        print(f'{estoque}')
        print("programa finalizado.")
        break
    else:
        print('Escolha de 1 a 4.') 
