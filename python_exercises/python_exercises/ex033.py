a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro númeor: '))

'''lista = [a, b, c]
lista.sort()

print('O maior número é {} e o menor número é {}'.format(lista[2], lista[0]))'''

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior =  c

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
