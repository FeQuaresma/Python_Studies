nome = str(input('Digite o nome do funcionário: ')).strip()
salario = int(input('Digite seu salário: '))

if salario <= 1250:
    print('O salário de {} vai receber um aumento de 15%, resultando em {}'.format(nome, salario*1.15))
else:
    print('O salário de {} vai receber um aumento de 10%, resultando em {}'.format(nome, salario*1.10))
    