km = float(input('Qual a distância em km da viagem: '))

if km <= 200:
    print('A sua viagem vai custar R$ 0.50 o km, resultando em R$ {:.2f}'.format(km*0.5))
else:
    print('A sua viagem vai custar R$ 0.45 o km, resultando em R$ {:.2f}'.format(km*0.45))
