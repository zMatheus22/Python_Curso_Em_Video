# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('\33[1:34:40m===== Desafio 006 =====\33[m')
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O número digitado \33[1:32:40m{}\33[m, o dobro é \33[1:32:40m{}\33[m, o triplo é \33[1:35:40m{}\33[m e a '
      'raiz quadrada \33[1:32:40m{:.3f}\33[m'.format(num, dobro, triplo, raiz))
