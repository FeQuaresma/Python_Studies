print()
tupla = ('Pão', 4.30,
        'Requeijão', 6.32,
        'Leite', 3.56,
        'Peixe', 54.14,
        'Carne', 90.13,
        'Castlevania: SOTN', 249.99)
soma = 0

for pos, item in enumerate(tupla):
    if pos % 2 != 0:
        soma += item

print('-'*50)
print('{:^50}'.format('Lista de compras'))
print('-'*50)
for pos, item in enumerate(tupla):
    if pos % 2 == 0:
        print('{:.<40} R$'.format(item), end='')
    else:
        print('{:>7.2f}'.format(item))
print('-'*50)
print('{:.<40} R$ {:>6.2f}'.format('Total', soma))
print()
