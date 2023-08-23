# Desenvolva um programa que pergunte a distãncia de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por
# Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

print('===== Desafio 031 =====')
distancia = float(input('Informe a distância: '))
if distancia <= 200:
    valor = 0.5 * distancia
    print('A com a distância de {},o valor do Km é R$ 0.50, o valor ficara R$ {:.2f}'
          .format(distancia, valor))
else:
    valor = 0.45 * distancia
    print('A com a distância de {}, maior que 200Km o valor fica R$ 0.45 o Km, o valor ficara R$ {:.2f}'
          .format(distancia, valor))
