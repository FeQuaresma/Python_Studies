n = int(input('Quantos elementos da sequência de fibonacci quer mostrar: '))
pt = 1
st = 1
tt = 2
count = 1
seq = '0 '
if n <= 0:
    print('Esse é um número inválido, tente novamente')

else:
    while count != n:
        seq += (f'> {pt} ')
        tt = pt + st
        pt = st
        st = tt
        count += 1
    print(seq)
