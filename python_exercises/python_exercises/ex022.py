nome = str(input('Qual é o seu nome? ')).strip()
separado = nome.split()
contagem = ''.join(separado)

print(nome.upper())
print(nome.lower())
#print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O nome tem {} letras'.format(len(contagem)))
print('O primeiro nome tem {} letras'.format(len(separado[0])))
