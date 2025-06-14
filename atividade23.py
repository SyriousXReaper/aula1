valor_compra = float(input('Digite o valor total da compra: '))
resposta = str(input('Escolha as opções de gorgeta A - 10%  B - 15%  C - 20%: '))
gorjeta = 0
if resposta == 'A' or 'a':
    gorjeta = valor_compra * 0.10
elif resposta == 'B' or 'b':
    gorjeta = valor_compra * 0.15
elif resposta == 'C' or 'c':
    gorjeta = valor_compra * 0.2
print(f'O valor da gorjeta será: {gorjeta}')
