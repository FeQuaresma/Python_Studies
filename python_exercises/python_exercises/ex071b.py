print('='*30)
print('{:^30}'.format('Banco'))
print('='*30)
saq = int(input('Qual o valor do saque? R$ '))
ced = 50
totalced = 0

while True:
    if saq >= ced:
        saq -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} de R$ {ced}')
        totalced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif saq == 0:
            break
print('Fim')
