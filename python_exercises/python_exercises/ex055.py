print()
peso = float(input('Insira um peso: '))
maior = peso
menor = peso
for c in range(0, 4):
    peso = float(input('Insira um peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print()
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')
print()
