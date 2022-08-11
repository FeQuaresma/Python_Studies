boletim = []
dados = []

while True:
   dados.append(str(input('Nome: ')))
   dados.append([])
   dados[1].append(float(input('Nota 1: ')))
   dados[1].append(float(input('Nota 2: ')))
   dados.append((dados[1][0]+dados[1][1])/2)
   boletim.append(dados[:])
   dados.clear()

   cont = str(input('Deseja cotinuar? [S/N] ')).upper()
   if cont[0] in 'N':
       break

print('-='*20)
print('No. ', f'{"Nome":<10}', 'Média')
print('-'*30)
for aluno in range(0, len(boletim)):
    print(f'{aluno:4}', f'{boletim[aluno][0]:<10}', f'{boletim[aluno][2]}')
print('-'*30)


while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if notas == 999:
        break
    print(f'Notas de {boletim[notas][0]} são {boletim[notas][1]}')
    print('-'*30)
  
print('Finalizando...','\n<<< Volte sempre >>>')
