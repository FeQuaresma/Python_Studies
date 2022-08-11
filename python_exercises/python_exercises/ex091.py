from random import randint
from time import sleep
jogador = {}
pos = 1

print('Valores Sorteados:')
for j in range(1, 5):
    jogador[f'jogador{j}'] = randint(1, 6)
    print(f'    O jogador{j} tirou {jogador[f"jogador{j}"]}')
    sleep(0.5)

lista = sorted(jogador.values(), reverse=True)
#for d in range(1, 5):
#    jogador[f'jogador{d}'] = lista[d-1]

print('Ranking dos jogadores:')


for k, v in jogador.items():
    print(f'    {pos}º lugar: {k} com {v}')
    pos += 1
    sleep(0.5)
