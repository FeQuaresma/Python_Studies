lista = []
par = []
impar = []
cont = 'S'
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper()
        if cont[0] not in 'SN':
            print('Não entendi...')
        else:
            break
    if cont == 'N':
       break

print()
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
