from math import hypot

ocat = float(input('Tamanho do cateto oposto: '))
acat = float(input('Tamanho do cateto adjacente: '))
hyp = hypot(ocat, acat)

print('O triângulo retângulo de {} por {} tem a hipotenusa de {:.2f}'.format(ocat, acat, hyp))
