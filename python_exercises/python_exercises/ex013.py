nome = input('Qual é o nome do funcionário? ')
n = float(input('Qual o seu salário? '))
print('O salário do {} de R$ {:.2f}\nAumentou em R$ {:.2f} (15%)\nResultou em R$ {:.2f}'.format(nome, n, n*0.15, n*1.15))
