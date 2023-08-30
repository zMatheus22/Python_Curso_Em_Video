# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 Anos: Junior
# - Até 25 Anos: Sênior
# - Acima: Master

from datetime import date

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 041 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('Sistema CNN - Nivelação')
print('\33[1:34m-\33[m'*23)

nascimento = int(input('\33[1:32mDigite o ano de nascimento do nadador: \33[m'))
idadeNadador = date.today().year - nascimento

if idadeNadador <= 9:
    print('\33[1:36m-'*23)
    print('Nível do nadador \33[4mMirim\33[m')
    print('\33[1:36m-\33[m'*23)
elif idadeNadador > 9 and idadeNadador <= 14:
    print('\33[1:36m-' * 23)
    print('Nível do nadador \33[4mInfantil\33[m')
    print('\33[1:36m-\33[m' * 23)
elif idadeNadador > 14 and idadeNadador <= 19:
    print('\33[1:36m-' * 23)
    print('Nível do nadador \33[4mJunior\33[m')
    print('\33[1:36m-\33[m' * 23)
elif idadeNadador <= 25:
    print('\33[1:36m-' * 23)
    print('Nível do nadador \33[4mSênior\33[m')
    print('\33[1:36m-\33[m' * 23)
else:
    print('\33[1:36m-' * 23)
    print('Nível do nadador \33[4mMaster\33[m')
    print('\33[1:36m-\33[m' * 23)

