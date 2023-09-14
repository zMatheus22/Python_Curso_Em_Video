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
