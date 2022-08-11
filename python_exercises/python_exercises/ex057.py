print()
sexo = ''
sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in('M','F'):
    sexo = str(input('Sexo não valído, digite novamente: [M/F] ')).upper().strip()[0]
print(f'Sexo {sexo} validado com sucesso')
print('Acabou')
