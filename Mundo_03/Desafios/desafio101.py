# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um voto literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições.




def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def voto(anoNascimento):
    from datetime import date

    '''
    Verifica se a pessoa está apeta a votar no brasil
    :param nascimento: Idade da pessoa
    :return: retorna o estado para voto da pessoa
    '''
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


menu('101', 'eleição')
nascimento = int(input('Ano de Nascimento: '))
print(f'{voto(nascimento)}')

