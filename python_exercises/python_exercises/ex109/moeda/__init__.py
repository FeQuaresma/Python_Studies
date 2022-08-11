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

