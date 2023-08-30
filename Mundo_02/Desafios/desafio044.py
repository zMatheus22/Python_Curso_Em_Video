# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

from datetime import date

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 044 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('   Sistema Lojistico')
print('\33[1:34m-\33[m'*23)

# Valor do produto
precoNormal = float(input('\33[1:36mValor do produto: R$ '))

# Opção de pagamento
print('\33[32m-'*23)
print('   Opção de Pagamento')
print(' 1 - Dinheiro ou Cheque')
print(' 2 - Cartão')
print('\33[1:32m-'*23)
opcaoPagamento = int(input('\33[1:36mDigite a opção: '))

# Valor final à pagar
precoAPagar = precoNormal

# Opção de pagamento: Dinheiro ou cheque
if opcaoPagamento == 1:
    precoAPagar = precoNormal - precoNormal * (10/100)
    print('\33[35m-' * 23)
    print('   Pagamento Dinheiro')
    print(' Ganhou 10% de Desconto')
    print('    Data: {}/{}/{}'.format(date.today().day, date.today().month, date.today().year))
    print('     Valor à pagar')
    print('      R$ {:.2f}'.format(precoAPagar))
    print('-' * 23)

# Opção de pagamento: Cartão
elif opcaoPagamento == 2:
    print('\33[32m-' * 23)
    print('     Opção do Cartão')
    print('1 - À vista')
    print('2 - Parcelado em 2x')
    print('3 - Parcelado em 3x ou mais')
    print('-' * 23)
    pacelaCartao = int(input('\33[1:36mDigite a opção: '))

    if pacelaCartao != 3:
        print('\33[35m-' * 23)
        print('    Pagamento Cartão')

    # Opção: À Vista
    if pacelaCartao == 1:
        precoAPagar = precoNormal - precoNormal * (5 / 100)
        print('        À Vista')
        print('  Ganhou 5% de Desconto')
    # Opção: 2x
    elif pacelaCartao == 2:
        print('    Parcelado em 2x')
    # Opção: 3x ou mais
    elif pacelaCartao == 3:
        quantidadeParcela = int(input('Informe a quantidade de parcelas: '))
        precoAPagar = precoNormal + precoNormal * (20 / 100)
        print('\33[35m-' * 23)
        print('    Pagamento Cartão')
        print('    Parcelado em {}x'.format(quantidadeParcela))
        print('  Juros de 5% no valor')
        print(' Parcelas de R$ {:.2f}'.format(precoAPagar/quantidadeParcela))

    # Apresentação do cartão
    print('    Data: {}/{}/{}'.format(date.today().day, date.today().month, date.today().year))
    print('     Valor à pagar')
    print('      R$ {:.2f}'.format(precoAPagar))
    print('-' * 23)
else:
    print('\33[1:31:40mERRO!\33[m')
