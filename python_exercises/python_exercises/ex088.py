from random import randint
from time import sleep

jogo = []

print('-'*30)
print(f'{"Mega Sena":^30}')
print('-'*30)

quant = int(input('Quantos jogos serão gerados: '))

for n in range(0, quant):
    jogo.append([])
    for num in range(0, 6):
        while True:
            r = randint(1, 60)
            if r not in jogo[n]:
                break
        jogo[n].append(r)
    jogo[n].sort()

print('-='*3, f'Sorteando {quant} jogos', '-='*3)

for hm in range(0, quant):
    print(f'Jogo {hm+1}: {jogo[hm]}')
    sleep(0.5)

print(f'{" < Boa sorte > ":-^30}')
