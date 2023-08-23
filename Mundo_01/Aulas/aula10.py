n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(media))
if media >= 6:
    print('Aluno passou! PARABÉNS!')
else:
    print('Aluno reprovado!')
