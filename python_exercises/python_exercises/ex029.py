vel = float(input('Velocidade do carro: '))
if vel > 80:
    print('Você está a {:.2f} km/h, acima do limite de velocidade.'.format(vel))
    print('A sua multa foi calculada em R$ {:.2f}'.format((vel - 80)*7))
print('Tenha um bom dia! Dirija com segurança')