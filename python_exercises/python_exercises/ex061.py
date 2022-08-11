# pt = int(input('Primeiro Termo: '))
# r = int (input('Razão: '))

# for c in range(pt, (pt+r*10), r):
#     print(c, end=' ')

# print('Fim')

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
rep = 0

while rep != 10:
   print(pt, end=' ')
   pt += r
   rep += 1
print('fim')
