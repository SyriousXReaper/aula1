notasCount = int(input("Digite a quantidades de notas para media: "))
soma = 0

for i in range(notasCount):
    
    nota = float(input("Digite as notas: "))
    soma += nota


media = soma / notasCount


print(f"A media e {media}")

