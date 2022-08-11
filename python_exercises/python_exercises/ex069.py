count = o18 = mens = wl20 = sexo = esc = 0

while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRO DE PESSOAS'))
    print('-'*30)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        o18 += 1
    while sexo not in('M', 'F'):
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        mens += 1
    if sexo == 'F' and idade < 20:
        wl20 += 1
    count += 1
    print('-' *30)
    while esc not in('S', 'N'):
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        print('-'*30)
        break
    esc = sexo = 0
print(f'Foram analisadas {count} pessoas')
print(f'São {o18} pessoas que tem mais de 18 anos')
print(f'São {mens} homens')
print(f'São {wl20} mulheres com menos de 20 anos')
print()
