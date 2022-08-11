print()
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print()

if media < 5:
    print('O aluno foi reprovado')

elif media > 5 and media < 7:
    print('O aluno está em recuperação')

else:
    print('O aluno está aprovado')
    
print(f'Sua média foi de {media:.1f}')

print()
