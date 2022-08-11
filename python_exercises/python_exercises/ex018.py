import math

ang = float(input('Qual é o ângulo: '))
ang = math.radians(ang)
print('O ângulo de {:.2f} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(ang, math.cos(ang), math.sin(ang), math.tan(ang)))
