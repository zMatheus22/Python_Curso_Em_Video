# aumentar(), diminuir(), dobrar(), metade()
def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')


def aumentar(valor, porcentagem, formatacao=False):
    '''
    -> Função serve para aumentar o valor informado pela procentagem informado.
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param porcentagem: (obrigadorio), porcentagem do valor a ser aumentado
    :param formatacao: (opcional), bool, formata o valor final para a aprecentação
    :return: o valor final com o aumento aplicado
    '''
    valorFinal = valor + (valor * (porcentagem / 100))
    if formatacao:
        return moeda(valorFinal)
    else:
        return valorFinal


def diminuir(valor, porcentagem, formatacao=False):
    '''
    -> Função serve para dar um desconto no valor informado com base na procentagem informada.
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param porcentagem: (obrigadorio), porcentagem de desconto do "valor"
    :param formatacao: (opcional), bool, formata o valor final para a aprecentação
    :return: o valor final com o deconto aplicado
    '''
    valorFinal = valor - (valor * (porcentagem / 100))
    if formatacao:
        return moeda(valorFinal)
    else:
        return valorFinal


def dobrar(valor, formatacao=False):
    '''
    -> Função para dobrar o valor informado
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param formatacao: (opcional), bool, formata o valor final para a aprecentação
    :return: o dobro do valor informado
    '''
    if formatacao:
        return moeda(valor*2)
    else:
        return valor*2


def metade(valor, formatacao=False):
    '''
    -> Função para informar a medate do valor
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param formatacao: (opcional), bool, formata o valor final para a aprecentação
    :return: a metade do valor informado
    '''
    if formatacao:
        return moeda(valor/2)
    else:
        return valor/2


def resumo(valor, aumeto=0, desconto=0):
    print('-'*30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print('{:<20}'.format('Preço analisado:'), end='')
    print('{:>10}'.format(f'{moeda(valor)}'))
    print('{:<20}'.format('Dobro do preço:'), end='')
    print('{:>10}'.format(f'{dobrar(valor,True)}'))
    print('{:<20}'.format(f'{aumeto}% de aumento:'), end='')
    print('{:>10}'.format(f'{aumentar(valor, aumeto, True)}'))
    print('{:<20}'.format(f'{desconto}% de redução:'), end='')
    print('{:>10}'.format(f'{diminuir(valor, desconto, True)}'))
    print('-' * 30)
