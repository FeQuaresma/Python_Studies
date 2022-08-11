from random import randint
contador = 1
x = randint(1,100)
z = int(input('A maquina escolheu um número, que numero????????!?1?1?!?!? '))
while True:
    if x == z:
        print(f'Dale c acertou, bixão memo, em {contador} tentativas')
        break
    else:
        if z < x:
            z = int(input('Errou trouxa, tenta de novo lixo, o n é maior '))
        elif z > x:
            z = int(input('Errou trouxa, tenta de novo lixo, o n é menor '))
        contador += 1
