# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 para cada km acima do limite.

print('===== Desafio 029 =====')
velocidade = float(input('Digite a velocidade do veículo: '))
multa = 7.00
limite = 80
if velocidade > limite:
    valorMulta = (velocidade - limite) * multa
    print('Você passou do limite da via, você recebera uma multa de R$ {:.2f}'.format(valorMulta))
print('FIM!')
