# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele.

print('\33[1:30:45m===== Desafio 004 =====\33[m')
dig = input('Digite algo: ')

print('Informações sobre o que foi digitado!!!')
print('O tipo primitivo desse valo é \33[1:30:45m{}\33[m'.format(type(dig)))
print('É alfanumérico? \33[1:30:45m{}\33[m'.format(dig.isalnum()))
print('É alfabético? \33[1:30:45m{}\33[m'.format(dig.isalpha()))
print('É ascii? \33[1:30:45m{}\33[m'.format(dig.isascii()))
print('É digito? \33[1:30:45m{}\33[m'.format(dig.isdigit()))
print('Esta em minúsculo? \33[1:30:45m{}\33[m'.format(dig.islower()))
print('É um decimal? \33[1:30:45m{}\33[m'.format(dig.isdecimal()))
print('É um identificador válido? \33[1:30:45m{}\33[m'.format(dig.isidentifier()))
print('É somente espaço? \33[1:30:45m{}\33[m'.format(dig.isspace()))
print('Todos os caracteres são imprimíveis? \33[1:30:45m{}\33[m'.format(dig.isprintable()))
print('Esta com a primeira letra maiúsculo? \33[1:30:45m{}\33[m'.format(dig.istitle()))
print('Esta maiúsculo? \33[1:30:45m{}\33[m'.format(dig.isupper()))
print('São todos número? \33[1:30:45m{}\33[m'.format(dig.isnumeric()))
