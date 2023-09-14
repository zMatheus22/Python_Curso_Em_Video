def leiaInt(msg):
    try:
        valorInt = input(msg).strip()
        while not valorInt.isnumeric():
            print('\33[1:31mValor informado não é um valor inteiro, tente novamente!')
            valorInt = input(msg)
    except KeyboardInterrupt:
        print('\33[31mUsuário não informou o número')
        valorInt = 0

    return int(valorInt)


def menuCadastro(lista):
    print('\33[34m-'*30)
    contador = 1
    for item in lista:
        print(f'\33[33m{contador} - \33[34m{item}')
        contador += 1
    print('\33[34m-' * 30)
    opcaoUser = leiaInt('\33[1:32mSua opção: ')
    return opcaoUser
