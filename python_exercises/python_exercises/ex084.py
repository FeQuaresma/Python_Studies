pessoas = []
dados = []
pesadas = []
leves = []
continuar = ''
pes = lev = 0

while True:

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if pesadas == [] or dados[1] == pes:
        pesadas.append(dados[0])
        pes = dados[1]

    elif dados[1] > pes:
        pesadas.clear()
        pesadas.append(dados[0])
        pes = dados[1]

    if leves == [] or dados[1] == lev:
        leves.append(dados[0])
        lev = dados[1]

    elif dados[1] < lev:
        leves.clear()
        leves.append(dados[0])
        lev = dados[1]
    
    dados.clear()
    continuar = str(input('Cotinuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {pes:.2f}kg. Peso de {pesadas}')
print(f'O menor peso foi {lev:.2f}kg. Peso de {leves}')
