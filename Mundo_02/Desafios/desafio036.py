# Escreva um progama para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 036 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
nome = str(input('\33[1:33mPor gentileza, infome o seu nome:\33[m '))
valorCasa = float(input('\33[1:33mPor gentileza, informe o valor da casa\33[m R$ '))
salario = float(input('\33[1:33mInforme o valor do seu salário\33[m R$ '))
anoEmprestimo = int(input('\33[1:33mInforme o tempo para o pagamento do empréstimo, em ano(s):\33[m '))
nome = nome.capitalize()
tempoEmprestimo = anoEmprestimo * 12
verificarEmprestimo = valorCasa / tempoEmprestimo
salario30por100 = salario * (30/100)

print('\33[1:34:40m=\33[m'*60)

if verificarEmprestimo > salario30por100:
    print('\33[1:31:40mInfelizmente {}, não será possivel realizar o emprestimo.\33[m'.format(nome))
    if salario == 0:
        print('\33[1:31:40mVocê não tem nem um limite para fazer empréstimo!\33[m')
    else:
        print('\33[1:31:40mPor questões de segurança, o empréstimo excede o valor de 30% do seu salário.\33[m')
        print('\33[1:31:40mO seu limite para o empréstimo é de R$ {:.2f} e o valor do empréstimo ficarou R$ {:.2f}\33[m'
              .format(salario30por100, verificarEmprestimo))

elif verificarEmprestimo <= salario30por100:
    print('\33[1:32:40mParabéns {}, o empréstimo foi aprovato!\33[m'.format(nome))
    print('\33[1:32:40mO valor do empréstimo será de R$ {:.2f} em {} messes ({} anos)\33[m'
          .format(verificarEmprestimo, tempoEmprestimo, anoEmprestimo))


