print()
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
menu = 0
print()
while menu != 5:
    print(f'''O que deseja fazer com {n1} e {n2}?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    menu = int(input('Opção escolhida: '))
    print()
    if menu == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
        print()
    elif menu == 2:
        print(f'A multiplicação de {n1} e {n2} é {n1 * n2}')
        print()
    elif menu == 3:
        if n1 > n2:
            print (f'{n1} é maior que {n2}')
        elif n2 > n1:
            print (f'{n2} é maior que {n1}')
        else:
            print('Os dois números são iguais')
        print()
    elif menu == 4:
        n1 = int(input('Insira novo número inteiro: '))
        n2 = int(input('Insira outro número inteiro: '))
        print()
    elif menu not in (1, 2, 3, 4, 5):
        print('Opção não é valída')
        print()
    if menu not in (4, 5):
        final = str(input('Deseja continuar? [S/N] ')).upper()
        if final == 'N':
            menu = 5
        print()
print('Fim')
print()
