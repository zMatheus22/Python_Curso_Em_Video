# For
'''for c in range(1, 10):
    print(c)
print('Fim For')

# While
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim While')
'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} par e {impar} impar')
