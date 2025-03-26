i = 0

maior = 0
while i < 3:
    numero = int(input("Digite o primeiro numero: "))
    i = i + 1
    

    if numero > maior:
        maior = numero


print(f"O maior numero é {maior}")
