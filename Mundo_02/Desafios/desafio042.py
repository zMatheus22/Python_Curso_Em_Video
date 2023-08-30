# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 042 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('  Análise de Triângulo')
print('\33[1:34m-\33[m'*23)

reta01 = float(input('\33[1:34mDigite o valor da 1° reta: '))
reta02 = float(input('Digite o valor da 2° reta: '))
reta03 = float(input('Digite o valor da 3° reta: \33[m'))

analise01 = (reta01 + reta02) > reta03
analise02 = (reta01 + reta03) > reta02
analise03 = (reta02 + reta03) > reta01

if analise01 and analise02 and analise03:
    print('\33[1:32m-'*23)
    print('     É um triângulo')
    if reta01 == reta02 or reta01 == reta03:
        if reta01 == reta03:
            print('     \33[4:40mEquilatero\33[m')
        elif reta01 != reta02 or reta01 != reta03:
            print('     \33[4:40mIsósceles\33[m')
    else:
        print('     \33[4:40mEscaleno\33[m')
    print('\33[1:32m-\33[m' * 23)
else:
    print('\33[1:31m-' * 23)
    print('   Não é um triângulo')
    print('\33[1:31m-\33[m'*23)

