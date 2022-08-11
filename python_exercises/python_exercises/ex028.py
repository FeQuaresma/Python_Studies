from random import randint
from time import sleep
sorteio = randint(0, 5)
num = int(input('\nQual número foi sorteado entre 0 e 5? '))

print('Processando...')
sleep(3)

if num == sorteio:
    print('\nParabéns, você acertou!')
else:
    print('\nQue pena, você errou!')

print('\nO número era {}!\n'.format(sorteio))
