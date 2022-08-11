print()
n = int(input('Digite um número: '))
primo = True
count = 0
lista = '\033[33m1\033[m'
print()

for c in range(2, n):
    if n % c == 0:
        primo = False
        count += 1
        lista += f' \033[33m{c}'
    else:
        lista += f' \033[31m{c}'
lista += f' \033[33m{n}\033[m'
print(lista)
if primo == True:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} foi divisível {count} vezes.')
    print(f'E por isso não é primo')
print()
