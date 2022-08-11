print()
s = 0
s1 = 0
for c in range (3, 501, 3):
    if c % 2 == 1:
       s += c
       s1 += 1
print(f'A soma dos {s1} números, resulta em {s}')
print()
