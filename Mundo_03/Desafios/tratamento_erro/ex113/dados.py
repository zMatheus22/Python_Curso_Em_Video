def leiaInt(msg):
    try:
        valorInt = input(msg).strip()
        while not valorInt.isnumeric():
            print('\33[1:31mValor informado não é um valor inteiro, tente novamente!')
            valorInt = input(msg)
    except KeyboardInterrupt:
        print('\33[31mUsuário não informou o número')
        valorInt = 0

    return valorInt


def leiaReal(msg):
    try:
        valorReal = str(input(msg)).replace(',', '.').strip()
        valorInteiro = valorReal.replace('.', '')
        while not valorInteiro.isnumeric():
            print('\33[31mValor informado não é um valor real, tente novamente!')
            valorReal = str(input(msg)).replace(',', '.').strip()
            valorInteiro = valorReal.replace('.', '')
    except KeyboardInterrupt:
        print('\33[31mUsuário não informou o número')
        valorReal = 0

    return float(valorReal)
