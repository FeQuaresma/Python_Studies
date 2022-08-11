val = []
maior = menor = 0

for p in range(0,5):
    val.append(int(input(f'Digite um valor para a {p}ª posição: ')))
    if p == 0:
        maior = menor = val[p]
    else:
        if val[p] > maior:
            maior = val[p]
        if val[p] < menor:
            menor = val[p]
print(f'Os valores digitados foram: ', end='')
for c in val:
    print(c, end=' ')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for pos, c in enumerate(val):
    if c == menor:
        print(pos, end=' ')
print()
print(f'O maior valor digitado foi {maior} na posição ', end='')
for pos, c in enumerate(val):
    if c == maior:
        print(pos, end=' ')
