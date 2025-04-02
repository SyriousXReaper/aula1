palavra = str(input("Digite uma palavra para ver a quantidadede vogais:")).upper()
quantidade = 0
vogais = "AEIOU"
for i in (palavra):
    if i in vogais:
        quantidade += 1


print(quantidade)