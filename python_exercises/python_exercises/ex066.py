print()
count = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Foram digitados {count} números que a soma deu {soma}')
