senhas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in senhas:
    while True:
        escolha = input(f'Senha {numero} Digite "p" para chamar o próximo ou "e" para encerrar: ')
        if escolha == 'p':
            break 
        elif escolha == 'e':
            print('Atendimento encerrado.')
            exit() 
        else:
            print('Opção inválida. Tente novamente.')

print('Todas as senhas foram chamadas!')
