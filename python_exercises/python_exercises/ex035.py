a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if (abs(a - b) < c < a + b) == True:
    print('É possível formar um triângulo com {}, {} e {}'.format(a, b, c))
else:
    print('Não é possível formar um trinângulo com {}, {} e {}'.format(a, b, c))
