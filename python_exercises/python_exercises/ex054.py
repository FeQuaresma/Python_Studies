from datetime import date
maior = 0
menor = 0
print()
for c in range(0, 7):
    ano = int(input('Insira o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print()
print(f'''Dessas 7 pessoas,
{maior} são de maioridade
{menor} são de menoridade''')
print()
