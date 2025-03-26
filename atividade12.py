nomeUsuario = str(input("Digite um nome de usuario: "))
senha = str(input("Digite uma senha: "))

print("\t----------Acessando o Sistema----------")

nomeSist = str(input("Digite seu usuario: "))
senhaSist = str(input("Digite sua senha: "))

if nomeSist == nomeUsuario and senha == senhaSist:
    print(f"Bem vindo {nomeUsuario}")

else:
    print("Usuario ou senha incorretos!")