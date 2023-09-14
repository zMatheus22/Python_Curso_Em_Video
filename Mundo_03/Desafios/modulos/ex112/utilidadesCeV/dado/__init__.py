def leiaDinheiro(texto):
    valor = str(input(texto)).replace(',', '.').strip()
    while valor.isalpha():
        print('\33[31mERRO! Digite um preço válido')
        valor = str(input(texto)).replace(',', '.').strip()
    return float(valor)
