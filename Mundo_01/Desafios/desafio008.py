# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

print('\33[1:32:40m===== Desafio 008 =====\33[m')
metro = float(input('\33[1:33:40mDigite o metro:\33[m '))
cent = metro * 100
mili = cent * 10
print('\33[1:34:40m\33[4mO metro é {:.1f} m, o centimetro é {:.1f} cm e o milímetro é {} mm\33[m'.format(metro, cent, mili))
