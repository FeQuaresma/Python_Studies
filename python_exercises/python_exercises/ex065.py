count = 0
media = 0
parar = '1'

while parar != 'N':
    n = int(input('Digite um número: '))
    if parar == '1':
        maior = n
        menor = n
    count += 1
    media += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    parar = str(input('Deseja continuar? [S/N] ')).upper()

print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'A média dos {count} números digitados foi {media/count:.2f}')
