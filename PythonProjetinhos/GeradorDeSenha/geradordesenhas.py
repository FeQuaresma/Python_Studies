import random
import string
especial = '!@#$%&'

def gerador(y):
    senha = []
    for c in range(y):
        x = random.randint(0,2)
        if x == 0:
            senha.append(random.choice(string.ascii_letters))
        elif x == 1:
            senha.append(str(random.randint(0,9)))
        elif x == 2:
            senha.append(random.choice(especial))
    return ''.join(senha)

digitos = int(input('Quantidade de digitos na sua senha: '))
quant = int(input('Quantidade de senhas geradas: '))

for c in range(quant):
    print('Senha:', gerador(digitos))
