while True:
    print('\nVocê está no primeiro laço.\n')
    opcao1 = input('Deseja sair dele? Digite sim para isso:')
    if opcao1 == 'sim':
        break  # Este break é do primeiro laço
    else:
        while True:
            print('\nVocê está no segundo laço.')
            opcao2 = input('\nDeseja sair dele? Digite sim para isso:')
            if opcao2 == 'sim':
                break  # Este break é do segundo laço
        print('Você saiu do segundo laço.')
print('\nVocê saiu do primeiro laço\n')