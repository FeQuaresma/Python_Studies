print()
print('Tabuada')
n = int(input('Digite um número inteiro: '))
t = int(input('Até que número você quer a tabuada: '))
print()

for c in range(1, t+1): # n x c = n*c
    print(f'{n} x {c:>2} = {n*c}')


print('Fim')
print()
