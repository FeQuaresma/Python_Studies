def leiadinheiro(msg):
    while True:
        dinheiro = input(msg).strip()
        if dinheiro.isnumeric():
            return float(dinheiro)
        else:
            print(f'ERRO: "{dinheiro}" é um preço inválido')

