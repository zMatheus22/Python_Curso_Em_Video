# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print('\33[1:36:40m=\33[m'*23)
print('\33[1:36:40m DESAFIO 037 - MUNDO 2 \33[m')
print('\33[1:36:40m=\33[m'*23)

print('\33[1:36m-\33[m'*23)
print('\33[1:36m   Conversão de Base\33[m')
print('\33[1:36m-\33[m'*23)

numeroUser = int(input('\33[1:33mPor gentileza digite o valor: \33[m'))

print('\33[1:36m-\33[m'*23)
print('\33[1:36m    Opeções\33[m')
print('\33[1:36m    1 - Binário\33[m')
print('\33[1:36m    2 - Octal\33[m')
print('\33[1:36m    3 - Hexadecimal\33[m')
print('\33[1:36m-\33[m'*23)

opecao = int(input('\33[1:33mDigite a opção: \33[m'))

if opecao == 1:
    binario = bin(numeroUser)
    binario = binario.removeprefix('0b')
    print('\33[1:34mO número \33[4m{}\33[m\33[1:34m decimal equivale a \33[4m{}\33[m\33[1:34m em binário\33[m'
          .format(numeroUser, binario))
elif opecao == 2:
    octal = oct(numeroUser)
    octal = octal.removeprefix('0o')
    print('\33[1:34mO número \33[4m{}\33[m\33[1:34m Decimal equivale a \33[4m{}\33[m\33[1:34m em octal\33[m'
          .format(numeroUser, octal))
elif opecao == 3:
    hexadec = hex(numeroUser)
    hexadec = hexadec.removeprefix('0x')
    print('\33[1:34mO número \33[4m{}\33[m\33[1:34m decimal equivale a \33[4m{}\33[m\33[1:34m em hexadecimal\33[m'
          .format(numeroUser, hexadec))
else:
    print('\33[1:30:41mERRO!\33[m')

print('\33[1:30:44mFim!\33[m')
