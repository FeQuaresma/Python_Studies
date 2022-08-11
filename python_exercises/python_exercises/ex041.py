print()
idade = int(input('Digite a idade do atleta: '))
print()

if idade <= 9:
    print('O atleta entra na categoria MIRIM')
elif idade <= 14:
    print('O atleta entra na categoria INFANTIL')
elif idade <= 19:
    print('O atleta entra na categoria JUNIOR')
elif idade <= 20:
    print('O atleta entra na categoria SÊNIOR')
elif idade <= 100:
    print('O atleta entra na categoria MASTER')
else:
    print('O atleta está MORTO')
print()
