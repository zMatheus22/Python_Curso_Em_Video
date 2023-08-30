# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\33[1:32:40m=\33[m'*23)
print('\33[1:32:40m DESAFIO 039 - MUNDO 2 \33[m')
print('\33[1:32:40m=\33[m'*23)
print('\33[1:32m-'*23)
print(' Alistamento militar')
print('\33[1:32m-\33[m'*23)

alistamento = 18

nome = str(input('\33[1:33mInforme o seu nome: '))
nome = nome.capitalize()
nascimento = int(input('A sua data de nascimento: '))
print('Você já fez aniversário este ano?\33[m')
aniversario = str(input('\33[1:30:43m(S) - Sim  (N) - Não\33[m\n'))
aniversario.upper()
ano = date.today()
idade = ano.year - nascimento

print('\33[1:32m-\33[m'*70)
if aniversario == 'N' and idade == 17:
    idade = 18
elif idade == alistamento:
    print('\33[1:34m{}, todo jovem que completa {} anos até 31 de Dezembro de {} teve se alistar!'
          .format(nome, idade, ano.year))
    print('O Exército Brasileiro está aguardando você para defender a pátria!\33[m')
elif idade < alistamento:
    tempo = alistamento - idade
    anoAlistamento = ano.year + tempo
    print('\33[1:34m{}, faltam {} ano(s) para o seu alistamento, ele deverá ocorrer em {}\33[m'
          .format(nome, tempo, anoAlistamento))
else:
    tempo = idade - alistamento
    anoAlistamento = ano.year - tempo
    print('\33[1:34m{}, você cumpriu sua missão!'.format(nome))
    print('Você se alistou no exército em {}, já faz {} ano(s) do seu alistamento!\33[m'.format(anoAlistamento, tempo))
