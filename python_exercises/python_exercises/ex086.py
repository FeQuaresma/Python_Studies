matriz = [[], [], []]

for x in range(0, 3):
    for y in range(0,3):
        matriz[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]: ^3}]', end='')
    print()
