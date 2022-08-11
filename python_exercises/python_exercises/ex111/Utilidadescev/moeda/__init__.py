def metade(n, formt=False):
    if formt == True:
        return f'R${n/2:.2f}'
    else:
        return n/2


def dobro(n, formt=False):
    if formt == True:
        return f'R${n*2:.2f}'
    else:
        return n*2


def aumentar(n, p=1, formt=False):
    if formt == True:
        return f'R${n*(1+(p/100)):.2f}'
    else:
        return n*(1+(p/100))


def reduzindo(n, p=1, formt=False):
    if formt == True:
        return f'R${n*(1-(p/100)):.2f}'
    else:
        return n*(1-p/100)


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, porca, porcr):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)
    print(f'{"Preço analisado:":20}{moeda(n)}')
    print(f'{"Dobro do Preço:":20}{moeda(dobro(n))}') 
    print(f'{"Metade do Preço:":20}{moeda(metade(n))}')
    print(f'{porca}{"% de aumento:":18}{moeda(aumentar(n, porca))}')
    print(f'{porcr}{"% de redução:":18}{moeda(reduzindo(n, porcr))}')
    print('-'*30)


