num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('Dezena de milhar: {}'.format(dm))


#print('Analisando o número {}'.format(num))
#print('Unidade: ', num[-1])
#print('Dezena: ', num[-2])
#print('Centena: ', num[-3])
#print('Milhar: ', num[-4])
