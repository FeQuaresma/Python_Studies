print()
pt = int(input('Primeiro Termo: '))
r = int (input('Razão: '))

for c in range(pt, (pt+r*10), r):
    print(c, end=' ')

print('Fim')
print()
