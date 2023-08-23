# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print('\33[1:34:40m===== Desafio 014 =====\33[m')
celsius = float(input('\33[1:40mDigite a \33[4:34mtemperatura em °C:\33[m '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 1.8) + 32
rankine = (celsius * 1.8) + 491.67
print('\33[1:40mA temperatura \33[4:34m{} °C\33[m'
      '\33[1:40m em celsius equivale a fahrenheit \33[4:32m{:.1f} °F\33[m'
      '\33[1:40m, a kelvin \33[4:33m{} K\33[m'
      '\33[1:40m e a rankine \33[4:35m{:.1f} °R\33[m'
      .format(celsius, fahrenheit, kelvin, rankine))
