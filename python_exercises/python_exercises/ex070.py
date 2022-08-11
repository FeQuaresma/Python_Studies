esc = soma = quant = omil = 0

print('=--='*8)
print('{:^30}'.format("Quaresma's Supermarket"))
print('=--='*8)
while True:
    nome = str(input('Digite o nome do produto: ')).capitalize().strip()
    while True:
        preco = float(input('Digite o valor do produto: R$ '))
        if preco > 0:
            break
    soma += preco
    quant += 1
    if preco > 1000:
        omil += 1
    if quant == 1 or preco < precobarato:
        nomebarato = nome
        precobarato = preco
    while esc not in('S', 'N'):
        print()
        esc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if esc == 'N':
            break
    print()
    esc = 0

print('-'*30)
print(f'O valor total da sua compra foi R$ {soma:.2f}')
print(f'{omil} produtos custam mais de R$ 1000.00')
print(f'{nomebarato} é o produto mais barato, R$ {precobarato:.2f}')
print('-'*30)
print('Obrigado pela compra, volte sempre!')
print()
