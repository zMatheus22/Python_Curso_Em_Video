def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivoTXT(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Erro ao criar o arquivo: {nome}')
    else:
        print(f'Arquivo: {nome} criado com sucesso!')


def escreverArquivo(arquivo, nome, idade):
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('\33[31mErro ao acessar os arquivos')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao tentar escrever no arquivo')
        else:
            print(f'Novo registro de {nome} e {idade}')


def lerArquivoTXT(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print(f'Erro ao abrir o arquivo: {nome}')
    else:
        print(f'{"  Nome":<20}{"    Idade":>10}')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>10}')
    finally:
        arquivo.close()
