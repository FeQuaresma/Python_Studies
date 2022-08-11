brasileirao = ('Palmeiras', 'Brangantino', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Ceará SC', 'Corinthians', 'Fluminense', 'Flamengo', 'Juventude', 'Internacional', 'América-MG', 'São Paulo', 'Sport Recife', 'Cuiabá', 'Chapecoense', 'Grêmio')
print(brasileirao[:5])
print(brasileirao[-4:])
print(sorted(brasileirao))
#n = ''
#for pos in range(0, len(brasileirao)):
#    if brasileirao[pos] == 'Chapecoense':
#        n = pos
#print(f'Chapecoense está na {n+1}ª posição')
print(f'Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')
