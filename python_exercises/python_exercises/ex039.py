from datetime import date

print()
nascimento = int(input('Que ano você nasceu? '))
ano = date.today().year
idade = ano - nascimento
print()

print(f'Quem nasceu em {nascimento}, tem {idade} em {ano}')
if idade < 18:
    print('Ainda não chegou a hora de se alistar')
    print(f'Falta {abs(idade - 18)} anos para seu alistamento')
    print(f'Você vai se alistar em {ano+(abs(idade-18))}')

elif idade == 18:
    print('Está na hora de se alistar')

else:
    print('Já passou da hora de se alistar')
    print(f'já se passaram {abs(idade - 18)} anos do seu alistamento')
    print(f'Seu alistamento foi em {ano-(abs(idade - 18))}')

print()
