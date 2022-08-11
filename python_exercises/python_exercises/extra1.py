n = input('vapo') #sem int
try:
  if (n != ''):
    n = int(n)
except:
  #aqui deu erro ao tentar converter pra int
  print('isso mesmo vadia, caguei nas calças')

print(n)
