def fatorial(numero=1):
    fatoria = 1
    for contador in range(numero, 0, -1):
        fatoria *= contador
    return fatoria


numeroUser = int(input('Digite o número: '))
print(f'O fatorial de {numeroUser} é {fatorial(numeroUser)}')
