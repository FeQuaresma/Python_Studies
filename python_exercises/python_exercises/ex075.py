par = ''
num = ''
print('Digite números entre 0 a 10')
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

tupla = (a, b, c, d)

for cont in tupla:
    if cont % 2 == 0:
        par += f'{cont} '


print(f'Os valores digitados foram {a}, {b}, {c}, {d}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print(f'O 3 foi digitado primeiro na {tupla.index(3)+1}º posição')
if par == '':
    print('Não tem números pares')
else:
    print(f'Os números pares foram {par}')
