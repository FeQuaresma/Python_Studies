matriz = [[], [], []]
pares = tercol = 0
mseglin = ''

for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x}, {y}]: '))

        if num % 2 == 0:
            pares += num

        if y == 2:
            tercol += num

        if x == 1 and (mseglin == '' or num > mseglin):
            mseglin = num

        matriz[x].append(num)

print(f'{"-="*10}')
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]: ^3}]', end='')
        if y == 2:
            print()
print(f'{"-="*10}')

print(f'A soma de todos os valores pares foi {pares}')
print(f'A soma de todos os valores da terceira coluna foi {tercol}')
print(f'O maior número da segunda linha é {mseglin}')
print()
