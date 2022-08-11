print()

print('Caixa eletrônico')
while True:
    saq = float(input('Quanto deseja sacar? R$ '))
    if saq - int(saq) > 0:
        print('Não temos centavos')
    else:
        break
saq = int(saq)

rs50 = saq // 50
saq -= rs50*50
rs20 = saq // 20
saq -= rs20*20
rs10 = saq // 10
saq -= rs10*10
rs1 = saq // 1
saq -= rs1*1

if rs50 > 0:
    print(f'Total de {rs50} cédulas de R$ 50')
if rs20 > 0:
    print(f'Total de {rs20} cédulas de R$ 20')
if rs10 > 0:
    print(f'Total de {rs10} cédulas de R$ 10')
if rs1 > 0:
    print(f'Total de {rs1} cédulas de R$ 1')
print()
