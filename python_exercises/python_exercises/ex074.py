from random import randint

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for t in tupla:
    print(f'{t} ', end='')
print()
print(f'O maior número é {sorted(tupla)[-1]}')
print(f'O menor número é {sorted(tupla)[0]}')
