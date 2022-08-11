from random import randint
print()

com = randint(1, 10)
jog = 0
count = 1

print('O computador pensou em um número de 1 a 10')
print('Descubra qual foi')
print()
jog = int(input('Qual o número o computador pensou? '))
while com != jog:
    if com > jog:
        print('Mais... ',end='')
    else:
        print('Menos... ', end='')
    jog = int(input('Tente novamente: '))
    count += 1

print()
if count > 1:
    print('Parabéns, você acertou!')
    print(f'Você precisou de {count} tentativas')
else:
    print('Parabéns, você acertou de primeira!')
print(f'O número era {com}')
