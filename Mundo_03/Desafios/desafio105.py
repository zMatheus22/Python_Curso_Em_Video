# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def notaAlunos(* notas, situacao=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param situacao: (valor opcional), indicando se deve ou não adicional a situação
    :return: dicionário com vários informações sobre a situação da turma.
    '''
    aluno = dict()
    aluno['total'] = len(notas)
    soma = 0
    for indece, nota in enumerate(notas):
        if indece == 0:
            aluno['maior'] = nota
            aluno['menor'] = nota
        elif aluno['maior'] < nota:
            aluno['maior'] = nota
        elif aluno['menor'] > nota:
            aluno['menor'] = nota
        soma += nota
    aluno['média'] = soma / aluno['total']
    if situacao:
        if aluno['média'] <= 5:
            aluno['situação'] = 'RUIM'
        elif aluno['média'] <= 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'BOA'
    return aluno


menu('105', 'Sistema escolar')
print(notaAlunos(7.5, 6, 9, situacao=True))
# help(notaAlunos)
