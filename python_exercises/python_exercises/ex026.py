frase = str(input('Digite uma frase: ')).strip()
#frase = str(input('Digite uma frase: ')).lower().strip()
cont = frase.lower().count('a')
achep = frase.lower().find('a')
acheu = frase.lower().rfind('a')

print('Aparece {} letras "a" na sua frase'.format(cont))
print('A primeira letra "a" aparece na posição {}'.format(achep + 1))
print('A última letra "a" aparece na posição {}'.format(acheu + 1))
