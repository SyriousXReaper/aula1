escolha = str(input('Adicione um item na sacola: '))
compras = escolha
while True:
    escolha2 = str(input('deseja adicionar outros itens? Sim ou Não: '))
    if escolha2 == 'Não':
        break
    else:
        compras.append(escolha)
print(f'Os itens da lista de compras são: {compras}')
