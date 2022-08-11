def soma(a, b):
    print(f'A recebe {a} e B recebe {b}')
    s = a + b
    print(f'A soma de é igual a {s}')
def contador(*num):
    print(f'Foram digitados {len(num)} números')
def dobra(lista):  
    pos = 0
    while pos <len (lista):
        lista[pos] *= 2
        pos += 1
    

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
