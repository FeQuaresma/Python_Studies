cpf = str(input('Digite seu CPF(Sem ponto e hífen): ')).strip()
cont = 10
digito = soma = 0
autentic = True

if len(cpf) != 11:
    autentic = False

while autentic:
    if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:
        autentic = False

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
        autentic = False

if autentic:
    print(f'O CPF {cpf} é válido')
else:
    print(f'O CPF {cpf} não é válido')
