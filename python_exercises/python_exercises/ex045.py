from random import randint
from time import sleep

print()
print('💎 🧻 ✂ ' * 6)
print('\033[1;31m{:^50}\033[m'.format('Jokenpô'))
print('💎 🧻 ✂ ' * 6)
print()
print('''O computador irá escolher entre pedra, papel e tesoura

Escolha:
1- 💎
2- 🧻
3- ✂''')
jor = int(input(''))
com = randint(1, 3)
print()

print('Processando...')
sleep(2)
print()

if jor in [1, 2, 3]:
    if (jor == 1 and com == 2) or (jor == 2 and com == 3) or (jor == 3 and com == 1):
        print('\033[31mO jogador perdeu!\033[m')
    elif (jor == 2 and com == 1) or (jor == 3 and com == 2) or (jor == 1 and com == 3):
        print('\033[32mO jogador ganhou!\033[m')
    else:    
        print('\033[33mO jogador e a máquina empataram\033[m')
    lista = ['💎', '🧻', '✂']
    print(f'A máquina escolheu {lista[com-1]}')

else:
    print('Jogador é um imbecil que não consegue seguir regras simples, vai se tratar garota sai da minha bota!')
print()
