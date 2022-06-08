#
import time as tm
import datetime
import os
import calendar
import pandas as pd
import json
import numpy as np

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
    }
df_dados = pd.DataFrame(dados)

def metodos_series():
    # Série criada na unha
    series_dados = pd.Series([10.2, -1, None, 15, 23.4])
    # Retorna uma tupla com o número de linhas
    print('Quantidade de linhas = ', series_dados.shape)
    # Retorna o tipo de dados, se for misto será object
    print('Tipo de dados', series_dados.dtypes)
    # Verifica se os valores são únicos (sem duplicações)
    print('Os valores são únicos?', series_dados.is_unique)
    # Verifica se existem valores nulos
    print('Existem valores nulos?', series_dados.hasnans)
    # Conta quantas valores existem (excluí os nulos)
    print('Quantos valores existem?', series_dados.count())
    # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
    print('Qual o menor valor?', series_dados.min())
    # Extrai o valor máximo, com a mesma condição do mínimo
    print('Qual o maior valor?', series_dados.max())
    # Extrai a média aritmética de uma Series numérica
    print('Qual a média aritmética?', series_dados.mean())
    # Extrai o desvio padrão de uma Series numérica
    print('Qual o desvio padrão?', series_dados.std())
    # Extrai a mediana de uma Series numérica
    print('Qual a mediana?', series_dados.median())
    # Exibe um resumo sobre os dados na Series
    print('\nResumo:\n', series_dados.describe())

def metodos1_dataframe():
    lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
    lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
    lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
    lista_idades = [32, 22, 25, 29, 38]
    pd.DataFrame(lista_nomes, columns=['nome'])
    pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)
    dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
    print(dados)
    print(pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email']))
    print(pd.DataFrame(dados))

def metodos2_dataframe():
    print('\nInformações do DataFrame:\n')
    # Apresenta informações sobre a estrutura do DF
    print(df_dados.info())
    s = input('...')
    # Retorna uma tupla com o número de linhas e colunas
    print('\nQuantidade de linhas e colunas = ', df_dados.shape)
    # Retorna o tipo de dados, para cada coluna, se for misto será object
    print('\nTipo de dados:\n', df_dados.dtypes)
    # Extrai o menor de cada coluna 
    print('\nQual o menor valor de cada coluna?\n', df_dados.min())
    # Extrai o valor máximo e cada coluna
    print('\nQual o maior valor?\n', df_dados.max())
    # Extrai a média aritmética de cada coluna numérica
    print('\nQual a média aritmética?\n', df_dados.mean())
    # Extrai o desvio padrão de cada coluna numérica
    print('\nQual o desvio padrão?\n', df_dados.std())
    # Extrai a mediana de cada coluna numérica
    print('\nQual a mediana?\n', df_dados.median())
    # Exibe um resumo
    print('\nResumo:\n', df_dados.describe())
    # Exibe os 5 primeiros registros do DataFrame
    print(df_dados.head())
    # Exibe os 5 últimos registros do DataFrame
    print(df_dados.tail())

def metodos3_dataframe():
    df_uma_coluna = df_dados['idades']
    print(type(df_uma_coluna))

    print('Média de idades = ', df_uma_coluna.mean())

    print(df_uma_coluna)
    colunas = ['nomes', 'cpfs']
    df_duas_colunas = df_dados[colunas]
    print(type(df_duas_colunas))
    print(df_duas_colunas)

# dfteste = pd.read_csv('https://github.com/isaiasavila/datasets/raw/main/wine_dataset.csv')
# print(dfteste)
# df = pd.read_csv('https://github.com/isaiasavila/datasets/raw/main/saidas.csv')
# print(df)
# local = pd.read_csv('utf8.csv')
# print(local['data'].nunique())
# dfm = (local.groupby(['data']).count())
# print(dfm['atividade'])
# print(local)

class Teste:
    
    def contar_string(self, _arquivo, _numeroString, _separador):
        '''
        Método retorna a maior string, recebendo um arquivo csv como parâmetro,
        a coluna que se deseja contar e um separador de string
        '''
        # zera o contador
        contador = 0
        # abre o arquivo que terá a contagem
        with open(_arquivo) as arqTemp:
                linhas = arqTemp.readlines()
        # inicia uma tupla para contagem
        tupla = ()
        # percorre todo o arquivo
        for item in linhas:
            # a tupla recebe a linha do arquivo separada pelo separador
            tupla = item.split(_separador)
            # recupera o tamanho da string da coluna especificada
            tamanho = len(tupla[_numeroString])
            # verifica o tamanho da string com o maior tamanho das verificações
            if tamanho > contador:
                # se o valor for maior, atribue para  a variável
                contador = tamanho
        # retorna a maior string verificada
        return contador

    def __init__(self, _arquivo="saidas.csv"):
        '''
        Constructor da classe que já cria uma lista na memória
        '''
        self.lista = self.visualizar_arquivo(_arquivo)
        with open(_arquivo) as arquivo:#, 'r', encoding='UTF-8'
            self.tabela_temporaria = arquivo.readlines()


    def visualizar_arquivo(self, filename):
        with open(filename) as arquivo:#, 'r', encoding='UTF-8'
            _lista = []

            while (linha := arquivo.readline().rstrip()):
                lst = linha.split(',')
                if len(lst[0]) < 5:
                    txt = ''
                    for i in range(5 - len(lst[0])):
                        txt += ' '
                    lst[0] = lst[0] + txt
                if len(lst[3]) > 55:
                    lst[3] = lst[3][0:52]+'...'
                else:
                    txt = ''
                    for i in range(55 - len(lst[3])):
                        txt += ' '
                    lst[3] = lst[3] + txt
                if len(lst[4]) > 26:
                    lst[4] = lst[4][0:23]+'...'
                else:
                    txt = ''
                    for i in range(26 - len(lst[4])):
                        txt += ' '
                    lst[4] = lst[4] + txt
                _lista.append(lst)
            _lista[0][1] = _lista[0][1] +'      '
            _lista[0][2] = _lista[0][2] +' '
        return _lista

    def imprimir_arquivo(self):
        '''
        Imprime a lista da memória em um formato de grade
        [1º parâmetro] lista com cinco colunas com os valores a serem impressos
        '''
        top = '╔'+('═'*7)+'╦'+('═'*12)+'╦'+('═'*7)+'╦'+('═'*57)+'╦'+('═'*28)+'╗'
        bot = '╚'+('═'*7)+'╩'+('═'*12)+'╩'+('═'*7)+'╩'+('═'*57)+'╩'+('═'*28)+'╝'
        print(top)
        print('║ '+self.lista[0][0]+' ║ '+ self.lista[0][1]+' ║ '+ self.lista[0][2] +' ║ '+ self.lista[0][3] +' ║ '+ self.lista[0][4]+' ║')
        print(bot)
        print(top)
        for lin in range(2,len(self.lista)):
            texto = '║ '
            for col in range(5):
                texto = texto + self.lista[lin][col] + ' ║ '
            print(texto)
        print(bot)

textao = 'desenvolvimento de cômpetências socioemocionais e cognitivas'
# print(len('algebra e funcoes na educacao basica'))
# print(len('50 ideias de filosofia que voce precisa conhecer'))
# print(len('analise estatistica com r para leigos'))
# x = Teste('saidas.tasker')
# x.imprimir_arquivo()
# tabela = x.tabela_temporaria
# texto = ''
# for i in range(len(tabela)):
#     tabela[i] = tabela[i].lower()
    # texto += tabela[i]
# print(tabela)
# with open('saidas.txt', 'w') as file_object:
#     file_object.write(texto)
# print('Sucesso!')

def metodos_requests_bs4():
    import requests
    from bs4 import BeautifulSoup

    texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
    # print(texto_string[:100])
    bsp_texto = BeautifulSoup(texto_string, 'html.parser')
    lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})

    # print(type(bsp_texto))
    # print(type(lista_noticias))
    # print(lista_noticias[5])
    dados = []

    for noticia in lista_noticias:
        data = noticia.contents[0].text.strip() + ', 2017' # Dessa informação <strong>Jan. 25 </strong> vai extrair Jan. 25, 2017
        comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
        explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
        url = noticia.find('a')['href']
        dados.append((data, comentario, explicacao, url))

    print(dados[1])
    lista_noticias[5].contents
    df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])
    print(df_noticias.shape)
    print(df_noticias.dtypes)
    print(df_noticias.head())

    url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
    dfs = pd.read_html(url)

    print(type(dfs))
    print(len(dfs))
    df_bancos = dfs[0]
    print(df_bancos.shape)
    print(df_bancos.dtypes)
    df_bancos.head()