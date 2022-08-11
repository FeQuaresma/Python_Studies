pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
rep = 0
termos = 0

while rep != termos + 10:
    print(pt, end=' ')
    pt += r
    rep += 1
    if rep == termos + 10:
        termos += int(input('\nQuantos termos você deseja ver a mais? [0 para] '))
print(f'Foram mostrados {termos +10} termos')
print('FIM')
