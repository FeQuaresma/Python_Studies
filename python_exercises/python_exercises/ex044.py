print()
produto = float(input('Digite o valor do produto: R$ '))
print()
print('Qual a forma de pagamento:')
print('-1 à vista no dinheiro')
print('-2 à vista no cartão')
print('-3 em até 2x no cartão')
print('-4 em 3x ou mais no cartão')
fp = int(input(''))
print()

if fp == 1:
    print(f'O seu produto de R$ {produto:.2f} vai sair por R$ {produto * 0.90:.2f}')
elif fp == 2:
    print(f'O seu produto de R$ {produto:.2f} vai sair por R$ {produto * 0.95:.2f}')
elif fp == 3:
    print(f'O seu produto vai sair por R$ {produto:.2f}')
elif fp == 4:
    parcelas = int(input('Número de parcelas: '))
    juros = produto * 1.20
    print()
    print(f'O seu produto de R$ {produto:.2f} vai sair por R$ {juros}')
    print(f'Cada parcela vai sair por R$ {juros / parcelas}')
else:
    print('ERROR, forma de pagamento não encontrada, tente novamente')

print()
