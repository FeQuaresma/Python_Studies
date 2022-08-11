dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
pdia = 60
pkm = 0.15
print('O total a pagar é R$ {:.2f}'.format(dia*pdia+km*pkm))
