'''
pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 20}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['peso'] = 80.5

print('For key e valor')
for key, valor in pessoas.items():
    print(f'{key} = {valor}')
'''
estado = dict()
brasil = list()

for quantidade in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().capitalize()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())

for estados in brasil:
    for key, valor in estados.items():
        print(f'{key.upper()}: {valor}')
