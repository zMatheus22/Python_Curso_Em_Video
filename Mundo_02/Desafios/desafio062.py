# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar O termos.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 062 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('PA v3.0'))
print('\33[1:34m-\33[m'*23)

primeiroTermo = int(input('Digite o primeiro termo: '))
razaoPa = int(input('Digite a razão da PA: '))

op = primeiroTermo
quantidadeTermo = 10
ultimoTremo = primeiroTermo + quantidadeTermo * razaoPa
indece = 1

print('\33[1:36m+'*23)
while quantidadeTermo != 0:
    if indece < 11:
        if indece < 10:
            print('{:^23}'.format(f'0{indece}°: {op}'))
        else:
            print('{:^23}'.format(f'{indece}°: {op}'))

    else:
        print('\33[1:36m+' * 23)
        quantidadeTermo = int(input('Você quer ver mais quantos termos? '))
        if quantidadeTermo > 0:
            ultimoTremo = op + quantidadeTermo * razaoPa
            while op != ultimoTremo:
                print('{:^23}'.format(f'{indece}°: {op}'))
                op += razaoPa
                indece += 1
        else:
            print('{:^23}'.format('Fim!'))
            quantidadeTermo = 0
    op += razaoPa
    indece += 1

