# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por Km rodado

print('\33[1:33:40m===== Desafio 015 =====\33[m')
print('\33[1:33:40m=\33[m'*35)
print('\33[1:33:40m     Calculo de locação de carro   \33[m')
print('\33[1:33:40m=\33[m'*35)
dia = int(input('\33[1:33:40mDigite por \33[4:33mquantos dias ficou com o veículo: \33[m'))
km = float(input('\33[1:33:40mDigite quantos \33[4:33mKm foram rodados: \33[m'))
calculo = dia * 60 + km * 0.15
print('\33[1:33:40mVocê ficou com o veículo por \33[4:32m{} dia(s) e rodou {:.2f} Km\33[m'
      '\33[1:33:40m, o valor ficou \33[4:32mR$ {:.2f}\33[m'.format(dia, km, calculo))
