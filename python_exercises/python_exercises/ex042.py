print()
r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))
print()

if (abs(r1 - r2)) < r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} podem formar um triângulo!')
    if r1 == r2 == r3:
        print('E esse triângulo será Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E esse triângulo será Isósceles!')
    else:
        print('E esse triângulo será Escaleno!')
else:
    print(f'As retas {r1}, {r2} e {r3} não podem formar um triângulo!')
print()
