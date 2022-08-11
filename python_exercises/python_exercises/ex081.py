lista = []
cont = 'S'
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if cont[0] not in 'SN':
            print('Não entendi...')       
        else:
            break

    if cont == 'N':
        break
print()
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista, nas posições ', end='')
    for p, c in enumerate(lista):
        if 5 == lista[p]:
            print(p, end=' ')
    print()

else:
    print('O número 5 não está na lista')