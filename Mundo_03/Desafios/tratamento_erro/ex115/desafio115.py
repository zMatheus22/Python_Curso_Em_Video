# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from lib.menuCadastro import *
from lib.arquivo import *
from lib.data import *
from menu import menu

nomeArquivo = 'pessoa.txt'

if not arquivoExiste(nomeArquivo):
    criarArquivoTXT(nomeArquivo)

menu('115', 'Cadastro de usuário')
opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pesssoa', 'Sair do Sistema']

while True:
    opcaoUser = menuCadastro(opcoes)
    print('-' * 30)
    if opcaoUser == 1:
        print('{:^30}'.format(f'Opção 0{opcaoUser}'))
        print('-' * 30)
        lerArquivoTXT(nomeArquivo)
    elif opcaoUser == 2:
        print('{:^30}'.format(f'Opção 0{opcaoUser}'))
        print('-' * 30)
        nome = leiaNome('\33[35mNome: ')
        idade = leiaIdade('\33[35mIdade: ')
        escreverArquivo(nomeArquivo, nome, idade)
    elif opcaoUser == 3:
        print('{:^30}'.format(f'Opção 0{opcaoUser}'))
        print('-'*30)
        print('{:^30}'.format('Tchau! Até mais.'))
        break
    else:
        print('\33[1:31mPor gentileza, informar um opção válido.')
