lista = []
cont = 'S'
while True:
    add = int(input('Digite um valor: '))
    if add in lista:
        print('Valor não foi registrado...')
    else:
        print('Valor registrado com sucesso...')
        lista.append(add)
    while True:
        cont = str(input('Deseja Continuar? [S/N] ')).upper()
        if cont in 'SN':
            break
        else:
            print('Não Entendi...', end='')

    if cont == 'N':
        break
print('Os valores digitados foram ', end='')
lista.sort()
for c in lista:
    print(c, end=' ')
