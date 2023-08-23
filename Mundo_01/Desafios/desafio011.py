# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('\33[1:33:40m===== Desafio 011 =====\33[m')
altura = float(input('Digite quantos metros de \33[4:33maltura\33[m tem a parete: '))
largura = float(input('Digite quantos metro de \33[4:33mlargura\33[m tem a parete: '))
quantidadeParede = int(input('Digite a \33[4:33mquantide de parete\33[m que terão que ser pintadas: '))
area = altura * largura
tinta = area * quantidadeParede / 2
print('\33[1:33mCom a área da parete tendo \33[4m{} m²\33[m'
      '\33[1:33m a quantidade de parede sendo de \33[4m{}\33[m'
      '\33[1:33m, será necessário \33[4m{} litro de tinta(s)\33[m'
      '\33[1:33m para pintar a(s) parete(s)!\33[m'
      .format(area, quantidadeParede, tinta))
