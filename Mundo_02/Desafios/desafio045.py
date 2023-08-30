# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 045 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('       Jokenpô')
print('    🤞   👊   🖐️')
print('\33[1:34m-\33[m'*23)
print('\33[1:36m+'*23)
print('    1- 🤞 (TESOURA)')
print('    2- 👊 (PEDRA)')
print('    3- 🖐️ (PAPEL)')
print('\33[1:36m+\33[m'*23)
opecaoUser = int(input('\33[1:32mDigite a opção: '))
computador = randint(1, 3)

# Pedra > Tesoura
# Tesoura > Papel
# Papel > Pedra
print('\33[35m-'*23)

if opecaoUser == computador:
    print('         \33[33mEmpate')
    print('          TIE')
    print('\33[35m-\33[m' * 23)
elif opecaoUser != computador:
    print('         Jokenpô')
    if opecaoUser == 1:
        if computador == 2:
            print('    VC: 🤞 \33[31mvs\33[33m 👊 :PC')
            print('      \33[31mGanhador PC')
            print('       GAME OVER')
            print('\33[35m-\33[m' * 23)
        elif computador == 3:
            print('    VC: 🤞 \33[31mvs\33[33m 🖐️ :PC')
            print('     \33[32mGanhador User')
            print('        Champion')
            print('\33[35m-\33[m' * 23)
    elif opecaoUser == 2:
        if computador == 1:
            print('    VC: 👊 \33[31mvs\33[33m 🤞 :PC')
            print('     \33[32mGanhador User')
            print('        Champion')
            print('\33[35m-\33[m' * 23)
        elif computador == 3:
            print('    VC: 👊 \33[31mvs\33[33m 🖐️ :PC')
            print('      \33[31mGanhador PC')
            print('       GAME OVER')
            print('\33[35m-\33[m' * 23)
    elif opecaoUser == 3:
        if computador == 1:
            print('    VC: 🖐️ \33[31mvs\33[33m 🤞 :PC')
            print('      \33[31mGanhador PC')
            print('       GAME OVER')
            print('\33[35m-\33[m' * 23)
        elif computador == 2:
            print('    VC: 🖐️ \33[31mvs\33[33m 👊 :PC')
            print('     \33[32mGanhador User')
            print('        Champion')
            print('\33[35m-\33[m' * 23)
    else:
        print('\33[1:31:40mERRO!\33[m')
