par = 0
impar = 0
for numeros in range(10):
    n = int(input(f'insira um número: '))
    par = n % 2
    if par == 0:
        par += 1
    else:
        impar += 1
print(f'São no total {par} números pares e {impar} impares')
