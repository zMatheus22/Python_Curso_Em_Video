nome = str(input('Qual é seu nome? '))
nome = nome.capitalize()
if nome == 'Matheus':
    print('Olá, {}!\nSeu nome é muito bom!'.format(nome))
elif nome in 'Maria João Pedro':
    print('Olá, {}!\nSeu nome é bem comum no Brasil.'.format(nome))
elif nome == 'Ana':
    print('Olá, {}!\nBelo nome!'.format(nome))
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia!')
