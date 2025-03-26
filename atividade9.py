num1 = int(input("Digite um numero: "))

operacao = input("Digite uma operacao: (x), (/), (+), (-)")

num2 = int(input("Digite um numero: "))

if operacao == "x":
    print(f"Resultado: {num1 * num2}")

elif operacao == "/":
    print(f"Resultado: {num1 / num2}")

elif operacao == "+":
    print(f"Resultado: {num1 + num2}")

elif operacao == "-":
    print(f"Resultado: {num1 - num2}")

else:
    print("Operador invalido!")