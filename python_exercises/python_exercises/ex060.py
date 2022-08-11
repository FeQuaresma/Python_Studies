print()
n = int(input('Digite um número: '))
fatorial = n
multi = 1
fatorados = '1'
print()

while n != multi:
    fatorial *= multi
    multi += 1
    fatorados += f'x{multi}'

print(fatorados)
print(f'O fatorial de {n} é igual a {fatorial}')
print()
