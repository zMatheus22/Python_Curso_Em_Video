'''
num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)

num.append(7)
print('Adicionando com "append"', num)

num.sort(reverse=True)
print('Organizando e invertendo, com "sort"', num)

num.insert(2, 0)
print('Com "insert" posição 2', num)

num.insert(2, 3)
print('Com "insert" posição 2', num)
num.remove(3)
print('Com "remove"', num)

print(len(num))
'''

'''
valores = []
valores.append(1)
valores.append(4)
valores.append(1)

for indece, valor in enumerate(valores):
    print(f'Na posição {indece} está o número {valor}!')
print('Fim da lista')
'''

a = [7, 1, 4, 1, 8]
# Realizar uma LIGAÇÃO
b = a
# Realizar uma CÓPIA
c = a[:]

print(f'Lista A Antes de mudar B: {a}')
b[2] = 3
c[4] = 5
print(f'Lista A Depois de mudar B: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')



