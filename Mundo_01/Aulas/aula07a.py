n1 = int(input('Um valor: '))
n2 = int(input('O segundo número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
re = n1 % n2
print('A soma é {}, o produto é {} e a divição é {:.3f}'.format(s, m, d))
# Formatar a quantidade de casas do float => {:.3f}
print('A potencia é {}, a divição inteira é {} e o resto da divição é {}'.format(p, di, re))
