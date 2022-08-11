print()
print('\033[;33m-='*20)
print('{:^40}'.format('Financiamento de casa'))
print('-='*20, '\033[m\n')

casa = float(input('Qual o valor da casa? R$ \033[32m'))
salario = float(input('\033[mQual é o seu salário? R$ \033[32m'))
anos = float(input('\033[mQuantos anos para pagar? \033[32m'))
prestacoes = casa / (anos * 12)
print()
print(f'''A casa no valor de R$ {casa:.2f}, vai ser parcelada em {anos:0f} anos
e vai resultar em R$ {prestacoes:.2f} por parcela''')
if prestacoes > salario * 0.3:
    print('\n\033[31mSeu financiamento foi negado.\033[m\n')
else:
    print('\n\033[36mSeu financiamento foi aceito.')
    print('\033[m')
