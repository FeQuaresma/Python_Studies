print()
f1 = str(input('Digite uma frase: ')).strip()
f2 = f1.lower().replace(' ', '')
count = int((len(f2)/2) + 1)
palindromo = True
print()

for c in range(0, count):
    if f2[c] != f2[-(1+c)]:
        palindromo = False

#print(palindromo)
#print(f2[0])
#print(f2[-1])   

if palindromo == True:
    print(f'A frase "{f1}" é um palindromo')
else:
    print(f'A frase "{f1}" não é um palindromo')
print()
