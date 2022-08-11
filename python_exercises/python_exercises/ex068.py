from random import randint
c = 0

while True:
    print('-='*20)
    print('Jogo de par ou ímpar')
    print('-='*20)
    
    esc = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]    
    n = int(input('Digite um número: '))

    com = randint(1, 10)
    soma = n + com
    print()
    
    print(f'Você jogou {n} e o computador jogou {com} somando {soma}')
    if soma % 2 == 0 and esc == 'P':
        print('Você escolheu Par,\nParabéns Você ganhou!')
        print()
        c += 1
    elif soma % 2 == 1 and esc == 'I':
        print('Você escolheu Ímpar,\nParabéns Você ganhou!')
        print()
        c += 1    
    else:
        break
print(f'Você perdeu... \nForam {c} vitórias consecutivas')        
print()
