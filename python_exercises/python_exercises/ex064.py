flag = 0
count = 0
soma = 0

while flag != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n != 999:
        soma += n
        count += 1
    flag = n

print(f'''A soma de todos os {count} números digitados, 
(desconsiderando o último) foi de {soma}''')
