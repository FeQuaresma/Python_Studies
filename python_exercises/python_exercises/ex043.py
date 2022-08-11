print()
peso = float(input('Digite seu peso em kilos: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso / alt ** 2
print()

print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obersidade mórbida')
print()
