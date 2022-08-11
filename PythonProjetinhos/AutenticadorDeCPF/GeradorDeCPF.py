from random import randint
cpf = str(randint(10000000000, 99999999999))
cont = 10
digito = soma = 0
autentic = True

if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:
    autentic = False

while autentic:

    while cont > 1:
        soma += int(cpf[digito]) * cont
        digito += 1
        cont -= 1
    soma = (soma * 10)%11

    if soma == 10:
        soma = 0

    if int(cpf[9]) == soma:
        cont = 11
        digito = soma = 0
    elif int(cpf[10]) == soma:
        break
    else:
        cpf = str(randint(10000000000, 99999999999))

if autentic:
    print(f'O CPF {cpf} é válido')
