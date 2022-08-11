# Tuplas são imutáveis
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

#for count in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[count]} na posição {count}')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
