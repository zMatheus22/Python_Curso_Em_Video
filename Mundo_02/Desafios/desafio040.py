# Crie um programa que leia duas notas de um alino e calcule sua média, mostrando uma mensafem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0 => Reprovado
# - Média entre 5.0 e 6.9 => Recuperação
# - Média 7.0 ou superior => Aprovado

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 040 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('    Sistema escolar')
print('    Notas do Aluno.')
print('    Notas de 0 a 10')
print('\33[1:34m-\33[m'*23)

primeiraNota = float(input('\33[1:36mInforme a Nota do 1° bimestre: '))
segundaNota = float(input('Informe a Nota do 2° bimestre: '))
terceiraNota = float(input('Informe a Nota do 3° bimestre: '))
quartaNota = float(input('Informe a Nota do 4° bimestre: \33[m'))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4
if media >= 7:
    print('\33[1:32m-'*23)
    print(' Média de {:.1f}'.format(media))
    print(' Aluno Aprovado! :)')
    print('\33[1:32m-\33[m'*23)
elif media > 5 and media < 7:
    print('\33[1:33m-' * 23)
    print(' Média de {:.1f}'.format(media))
    print(' Aluno em Recuperação! :|')
    print('\33[1:33m-\33[m' * 23)
else:
    print('\33[1:31m-' * 23)
    print(' Média de {:.1f}'.format(media))
    print(' Aluno foi Reprovado! :(')
    print('\33[1:31m-\33[m' * 23)
