def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Número: '))

print(f'fatorial de {n} é {fatorial(n)}')

r1 = fatorial(5)
r2 = fatorial(4)
r3 = fatorial()
