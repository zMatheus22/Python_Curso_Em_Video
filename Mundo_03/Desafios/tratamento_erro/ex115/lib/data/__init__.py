def leiaNome(msg):
    try:
        while True:
            nome = str(input(msg)).strip().capitalize()
            if nome.isalpha():
                break
            print('\33[31mPor gentileza informar um Nome válida.')
    except:
        print('\33[31mErro! nome não informada.')
    else:
        return nome


def leiaIdade(msg):
    try:
        while True:
            idade = str(input(msg))
            if idade.isnumeric():
                break
            print('\33[31mPor gentileza informar um Idade válida.')
    except:
        print('\33[31mErro! idade não informada.')
    else:
        return int(idade)
