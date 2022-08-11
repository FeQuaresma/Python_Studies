frase1 = str(input('Digite uma frase: ')).strip()
frase1 = frase1.upper().replace(' ','')
frase2 = list(frase1)
frase2.reverse()
frase2 = ''.join(frase2)
print(f'Analisando {frase1} e {frase2}')
if frase1 == frase2:
    print('palindromo porra')
else:
    print('Não é palindromo')
