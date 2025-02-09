idade = eval(input('\nInforme a idade da criança: \n'))
if idade < 5:
    print('\nA criança precisa ser vacinada contra a gripe.')
    print('\nProcure o posto de saúde mais próximo.\n')
elif idade == 5:
    print('\nA vacina estará disponível em breve.')
    print('\nAguarde as próximas informações.\n')
else:
    print('\nA vacinação só ocorrerá daqui a 3 meses.')
    print('\nInforme-se novamente neste prazo.\n')
print('Cuide da saúde sempre. Até a próxima!\n')