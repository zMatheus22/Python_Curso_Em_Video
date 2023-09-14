# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 077 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Vogais nas palavras'))
print('\33[1:34m-\33[m'*23)

palavrasTecnologia = ('Tecnica', 'Ciencia', 'Conhecimento', 'Automaçao', 'Holograma', 'Cibercultura', 'Telematica',
                      'Algoritmo', 'Big data', 'Cibersegurança', 'Antivirus', 'Aplicativo', 'Backup', 'Iniciar')

for palavra in palavrasTecnologia:
    print(f'A palavra \33[4:32m{palavra.upper()}\33[m, tem as seguintes vogais: ', end='')
    vogais = ''
    for letra in range(len(palavra)):
        vogais = palavra[letra].lower()
        if vogais in ('a', 'e', 'i', 'o', 'u'):
            print(f'\33[4:32m{vogais}\33[m', end=' ')

    print('\n')
