
classe = []
alunos = ("Rafael", "Maria", "Pedro", "Paulo", "Miguel", "Vitoria")

for aluno in alunos:
    resposta = input(f"{aluno} Faltou ou está Presente?: ")
    if resposta == "presente":
        classe.append(aluno)

print(f"Total de alunos presentes: {classe}")

buscar = input("Deseja buscar o nome de um aluno? s ou n: ")
if buscar == "s":
    nome = input("Digite o nome do aluno: ")
    if nome in classe:
        print(f"{nome} estava presente.")
    else:
        print(f"{nome} faltou.")
else:
    print(f"total de alunos presentes {classe}")
