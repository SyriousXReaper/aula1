numero = int(input("Digite um numero para ver seu fatorial:"))
resultado = 1
for i in range(2, numero + 1):
    
    resultado *= i

print(resultado)