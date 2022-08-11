valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}!')
print('Fim')
