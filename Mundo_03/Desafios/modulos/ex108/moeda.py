# aumentar(), diminuir(), dobrar(), metade()
def aumentar(valor, porcentagem):
    '''
    -> Função serve para aumentar o valor informado pela procentagem informado.
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param porcentagem: (obrigadorio), porcentagem do valor a ser aumentado
    :return: o valor final com o aumento aplicado
    '''
    return valor + (valor * (porcentagem/100))


def diminuir(valor, porcentagem):
    '''
    -> Função serve para dar um desconto no valor informado com base na procentagem informada.
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :param porcentagem: (obrigadorio), porcentagem de desconto do "valor"
    :return: o valor final com o deconto aplicado
    '''
    return valor - (valor * (porcentagem/100))


def dobrar(valor):
    '''
    -> Função para dobrar o valor informado
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :return: o dobro do valor informado
    '''
    return valor * 2


def metade(valor):
    '''
    -> Função para informar a medate do valor
    :param valor: (obrigadorio), float, valor de algum "item" informado pelo usuário
    :return: a metade do valor informado
    '''
    return valor / 2


def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
