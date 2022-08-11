lista = []

for c in range(0,5):
    num = int(input('Digite um número: '))
    if lista == [] or num >= lista[-1]:
        print('Adicionado a última posição')
        lista.append(num)
    else:
        for p, n in enumerate(lista):
            if num < n:
                lista.insert(p,num)
                print(f'O valor foi adicionado na posição {p}')
                break

print(f'Os valores digitados foram {lista}')
