expr = str(input('Digite uma expressão: '))
cod = []
for l in expr:
    if l == '(':
        cod.append(l)
    elif l == ')':
        if cod == []:
            cod = [')']
            break
        cod.pop()

if cod == []:
    print('Essa é uma expressão valída!')
else:
    print('Está não é uma expressão valída!')
