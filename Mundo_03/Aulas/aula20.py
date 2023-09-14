'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
print('-'*20)
soma(b=8, a=9)

def contador(* num):
    tamanho = len(num)
    print(f'Os numeros {num} com o tamanho é {tamanho}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

def soma(* valores):
    somarValores = 0
    for numero in valores:
        somarValores += numero
    print(f'Somando os {valores} é igual a {somarValores}')


soma(2, 4)
soma(1, 3, 4, 6)
