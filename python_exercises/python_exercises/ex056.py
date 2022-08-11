print()
media = 0
maioridade = 0
velho = ''
menoridade = 0

for c in range(0, 4):
    nome = str(input('Qual o nome: ')).strip()
    idade = int(input('Qual a idade: '))
    sexo = int(input('Qual o sexo (sendo 0 homem, 1 mulher e 2 não-binário): '))
    media += idade
    if idade > maioridade and sexo == 0:
        maioridade = idade
        velho = nome
    if sexo == 1 and idade < 20:
        menoridade += 1
    print()

print(f'A média das idades é {media / 4:.1f}')
print(f'O nome do homem mais velho é {velho}')
print(f'{menoridade} mulheres tem menos que 20 anos')
print()
