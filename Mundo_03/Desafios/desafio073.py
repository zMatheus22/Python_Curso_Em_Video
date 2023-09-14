# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Grêmio (Chapecoense, estava na série B).

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 073 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Campeonato Brasileiro 2023'))
print('\33[1:34m-\33[m'*23)

classificacao = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza',
                 'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia',
                 'Santos', 'Vasco', 'Coritiba', 'América-MG')
print('\33[1:33m+'*23)
print('Times do Brasileirão')
for time in range(len(classificacao)):
    print(f'{time+1}° - {classificacao[time]}')

print('\33[1:32m+'*23)
print('Os 5 Primeiros times do Brasileirão')
for top5 in range(0, 5):
    print('{:^23}'.format(classificacao[top5]))

print('\33[31m+'*23)
print('Os últimos 4 da classificação do Brasileirão')
ultimos4 = len(classificacao)-4
for time in range(ultimos4, len(classificacao)):
    print('{:^23}'.format(classificacao[time]))

print('\33[36m+'*23)
print('Os times do Brasileirão em Ordem alfabética')
timesOrdem = sorted(classificacao)
for time in timesOrdem:
    print('{:^23}'.format(time))

print('\33[35m+'*23)
for time in range(len(classificacao)):
    if classificacao[time] == 'Grêmio':
        print(f'O {classificacao[time]} está na possição: {time + 1}°')
