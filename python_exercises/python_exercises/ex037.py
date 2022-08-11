print()
n = int(input('\nDigite um número: '))

print('''\n-1 para binário
-2 para octal
-3 para hexadecimal\n''')

bc = int(input('Escolha a base de conversão: '))

if bc == 1:
    print(f'{n} em binário é {n:b}')

elif bc == 2:
    print(f'{n} em octal é {n:o}')

elif bc == 3:
    print(f'{n} em hexadecimal é {n:x}')

else:
    print('Base de conversão não encontrada, tente novamente')
print()