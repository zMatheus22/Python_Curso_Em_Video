# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date

print('===== Desafio 032 =====')
ano = int(input('Digite o ano, se digitar "0" será o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 & ano % 100 != 0 | ano % 400 == 0:
    print('O ano é BISSEXTO!')
else:
    diferenca = 4 - ano % 4
    proximo = ano + diferenca
    print('Ano NÃO é BISSEXTO!')
    print('Faltam {} ano(s) para o próximo ano bissexto, será em {}.'.format(diferenca, proximo))
