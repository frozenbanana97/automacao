from datetime import date
from datetime import datetime as dt
import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
print(df_selic.info())
data_extracao = date.today()
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autora"
print(df_selic.info())
print(df_selic.head())
df_selic2 = df_selic
df_selic2['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic2['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')
print(df_selic2.info())
df_selic2['responsavel'] = df_selic['responsavel'].str.upper()
print(df_selic2.head())
df_selic2.sort_values(by='data', ascending=False, inplace=True)
print(df_selic2.head())
df_selic2.reset_index(drop=True, inplace=True)
print(df_selic2.head())
lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
print(lista_novo_indice[:5])
df_selic.set_index(keys=[lista_novo_indice], inplace=True)
print(df_selic.head())
print(df_selic['valor'].idxmin())
print(df_selic['valor'].idxmax())
print(df_selic.loc['selic_0'])
print(df_selic.loc[['selic_0', 'selic_4', 'selic_200']])
print(df_selic.loc[:'selic_5'])
#df_selic.loc[['selic_0', 'selic_4', 'selic_200']]['valor']
#df_selic.loc[['selic_0', 'selic_4', 'selic_200']][['valor', 'data_extracao']
print(df_selic.loc[['selic_0', 'selic_4', 'selic_200'], 'valor'])
print(df_selic.loc[['selic_0', 'selic_4', 'selic_200'], ['valor', 'data_extracao']])
print(df_selic.iloc[:5])
teste = df_selic['valor'] < 0.01
print(type(teste))
print(teste[:5])
teste2 = df_selic['data'] >= pd.to_datetime('2020-01-01')
print(type(teste2))
print(teste2[:5])
teste3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))
teste4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))
print("Resultado do AND:\n")
print(teste3[:3])
print("Resultado do OR:\n")
print(teste4[:3])
filtro1 = df_selic['valor'] < 0.01
df_selic.loc[filtro1]
data1 = pd.to_datetime('2020-01-01')
data2 = pd.to_datetime('2020-01-31')
filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
print(df_janeiro_2020.head())
data1 = pd.to_datetime('2019-01-01')
data2 = pd.to_datetime('2019-01-31')
filtro_janeiro_2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
print(df_janeiro_2019.head())
print('Mínimo geral = ', df_selic['valor'].min())
print('Mínimo janeiro de 2019 = ', df_janeiro_2019['valor'].min())
print('Mínimo janeiro de 2020 = ',df_janeiro_2020['valor'].min(), '\n')
print('Máximo geral = ', df_selic['valor'].max())
print('Máximo janeiro de 2019 = ', df_janeiro_2019['valor'].max())
print('Máximo janeiro de 2020 = ',df_janeiro_2020['valor'].max(), '\n')
print('Média geral = ', df_selic['valor'].mean())
print('Média janeiro de 2019 = ', df_janeiro_2019['valor'].mean())
print('Média janeiro de 2020 = ',df_janeiro_2020['valor'].mean(), '\n')

def mesmo_codigo_acima():

    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
    data_extracao = date.today()
    df_selic['data_extracao'] = data_extracao
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['data_extracao'] = pd.to_datetime(df_selic['data_extracao'])
    df_selic.sort_values(by='data', ascending=False, inplace=True)
    df_selic.reset_index(drop=True, inplace=True)
    lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novo_indice], inplace=True)
    print(df_selic['valor'].idxmin())
    print(df_selic['valor'].idxmax())
    filtro1 = df_selic['valor'] < 0.01
    print(df_selic.loc[filtro1])

# https://www.portaldatransparencia.gov.br/
# https://www.dados.gov.br/dataset
# https://archive.ics.uci.edu/ml/datasets.php
# https://vincentarelbundock.github.io/Rdatasets/datasets.html

def conexao_pandas_db_sql():
    # Postgres
    import psycopg2
    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"dbname='{database}' user='{username}' host='{host}' password='{password}' port='{port}'"
    conn = psycopg2.connect(conn_str)

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)
    # Mysql
    import mysql.connector

    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)

    def dados_perdidos():
        df = pd.read_csv('caminho_do_arquivo',sep=';',encoding='ISO-8859-1')
        # inplace altera o próprio df utilizado
        df.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)
        # seta a coluna ano como o indexador do dataframe
        df.set_index(keys='ANO', drop=True, inplace=True)
        # Percorre a coluna dos meses para alterar o separador de décimos/centésimos
        for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
            df[mes] = df[mes].str.replace(',', '.')
        # alterando o tipo de dados da coluna para número flutuante
        df = df.astype(float)
        # Em cada ano, qual o menor e o maior valor arrecadado da exportação?
        for ano in range(2012, 2021):
            ano_info = df.loc[ano]
            minimo = ano_info.min()
            maximo = ano_info.max()
            print(f"Ano = {ano}")
            print(f"Menor valor = {minimo:,.0f}".replace(',', '.'))
            print(f"Maior valor = {maximo:,.0f}".replace(',', '.'))
            print("--------------")
        # Considerando o período de 2012 a 2019, qual a média mensal de arrecadamento com a exportação
        print("Média mensal de rendimentos:")
        for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split():
            media = df.loc[2012:2019, mes].mean()
            print(f"{mes} = {media:,.0f}".replace(',', '.'))
        # Considerando o período de 2012 a 2019, qual ano teve o menor arrecadamento? E o menor?
        ano_menor_arrecadacao = df.loc[2012:2019, 'TOTAL'].idxmin()
        ano_maior_arrecadacao = df.loc[2012:2019, 'TOTAL'].idxmax()
        print(f"Ano com menor arrecadação = {ano_menor_arrecadacao}")
        print(f"Ano com maior arrecadação = {ano_menor_arrecadacao}")


def plotagem():
    import random
    from matplotlib import pyplot as plt
    dados1 = random.sample(range(100), k=20)
    dados2 = random.sample(range(100), k=20)
    plt.plot(dados1, dados2)
    import numpy as np
    x = range(5)
    x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.
    fig, ax = plt.subplots(1, 2, figsize=(12, 5)) # Cria figura com subplots: 1 linha, 2 colunas e eixos
    print("Tipo de ax = ", type(ax))
    print("Conteúdo de ax[0] = ", ax[0])
    print("Conteúdo de ax[1] = ", ax[1])
    ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
    ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
    ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
    ax[0].set_xlabel('Eixo x')
    ax[0].set_ylabel('Eixo y')
    ax[0].set_title("Gráfico 1")
    ax[0].legend()
    ax[1].plot(x, x, 'r--', label='eq_1') # cria gráfico sobre eixo 1
    ax[1].plot(x**2, x, 'b--', label='eq_2') # cria gráfico sobre eixo 1
    ax[1].plot(x**3, x, 'g--', label='eq_3') # cria gráfico sobre eixo 1
    ax[1].set_xlabel('Novo Eixo x')
    ax[1].set_ylabel('Novo Eixo y')
    ax[1].set_title("Gráfico 2")
    ax[1].legend()
    x = range(5)
    x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.
    fig = plt.subplots(figsize=(12, 5)) # Cria figura sem eixo
    plt.subplot(121) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 1           
    plt.plot(x, x, label='eq_1')
    plt.plot(x, x**2, label='eq_2')
    plt.plot(x, x**3, label='eq_3')
    plt.title("Gráfico 1")
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.legend()
    plt.subplot(122) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 2            
    plt.plot(x, x, 'r--', label='eq_1')
    plt.plot(x**2, x, 'b--', label='eq_2')
    plt.plot(x**3, x, 'g--', label='eq_3')
    plt.title("Gráfico 2")
    plt.xlabel('Novo eixo x')
    plt.ylabel('Novo eixo y')
    plt.legend()
    #
    import pandas as pd
    dados = {
        'turma':['A', 'B', 'C'],
        'qtde_alunos':[33, 50, 45]
        }
    df = pd.DataFrame(dados)
    print(df)
    df.plot(x='turma', y='qtde_alunos', kind='bar')
    df.plot(x='turma', y='qtde_alunos', kind='barh')
    df.plot(x='turma', y='qtde_alunos', kind='line')
    df.set_index('turma').plot(y='qtde_alunos', kind='pie')
    # dataset perdido? ######################
    df_etanol = pd.read_csv('exportacao-etanol-hidratado-2012-2020-bep.csv', sep=';', encoding="ISO-8859-1")
    # Apaga colunas que não usaremos
    df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)
    # Substitui a vírgula por ponto em cada coluna
    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
        df_etanol[mes] = df_etanol[mes].str.replace(',', '.')
    # Converte os valores para float
    df_etanol = df_etanol.astype(float)
    # Converte o ano para inteiro
    df_etanol['ANO'] = df_etanol['ANO'].astype(int)
    df_etanol.head(2)
    df_etanol.plot(x='ANO',
               y='JAN',
               kind='bar',
               figsize=(10, 5),
               rot=0,
               fontsize=12,
               legend=False)
    df_etanol.plot(x='ANO',
                y='JAN',
                kind='line',
                figsize=(10, 5),
                rot=0,
                fontsize=12,
                legend=False)
    df_etanol[['ANO', 'JAN', 'FEV']].plot(x='ANO', kind='bar', figsize=(10, 5), rot=0, fontsize=12)
    ############################ Seaborn
    import seaborn as sns
    # Configurando o visual do gráfico. Leia mais em https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set
    sns.set(style="whitegrid") # opções: darkgrid, whitegrid, dark, white, ticks
    df_tips = sns.load_dataset('tips')
    print(df_tips.info())
    df_tips.head()
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(x="day", y="total_bill", data=df_tips)
    ax.axes.set_title("Venda média diária", fontsize=14)
    ax.set_xlabel("Dia", fontsize=14)
    ax.set_ylabel("Venda média ", fontsize=14)
    ax.tick_params(labelsize=14)
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_tips, x="day")
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_tips, x="day", hue="sex")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df_tips, x="total_bill", y="tip")
    # Seção 6 ####################################################
def secao_seis():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    df_satelites = pd.read_csv('satelites_operando_comercialmente.csv', sep=';') 
    df_satelites.drop_duplicates(inplace=True)
    df_satelites.reset_index(drop=True, inplace=True)
    print(df_satelites.info())
    print(df_satelites.head())
    # Quantos satélites são brasileiros e quantos são estrangeiro?
    plt.figure(figsize=(5,3))
    plt.tick_params(labelsize=12)
    sns.countplot(data=df_satelites, x='Direito')
    # quantos satétiles cada operadora brasileira possui operando?
    df_satelites_brasileiros = df_satelites.loc[df_satelites['Direito'] == 'Brasileiro']
    plt.figure(figsize=(15,5))
    plt.xticks(rotation=90)
    plt.tick_params(labelsize=12)
    sns.countplot(data=df_satelites_brasileiros, x='Operadora Comercial')
    # Quantos satélites brasileiros estão operando em cada banda?
    plt.figure(figsize=(15,5))
    plt.xticks(rotation=90)
    plt.tick_params(labelsize=12)
    sns.countplot(data=df_satelites_brasileiros, x='Bandas')
    # Quantos satétiles cada operadora estrangeira possui operando?
    df_satelites_estrangeiros = df_satelites.loc[df_satelites['Direito'] == 'Estrangeiro']
    plt.figure(figsize=(15,5))
    plt.xticks(rotation=90)
    plt.tick_params(labelsize=12)
    sns.countplot(data=df_satelites_estrangeiros, x='Operadora Comercial')
    # Quantos satélites brasileiros estão operando em cada banda?
    plt.figure(figsize=(15,5))
    plt.xticks(rotation=90)
    plt.tick_params(labelsize=12)
    sns.countplot(data=df_satelites_estrangeiros, x='Bandas')
###
def teste():
    # bibliotecas importadas
    from datetime import datetime
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    # acessa o portal e utiliza a propriedade text para capturar no formato desejado
    texto_string = requests.get('https://globoesporte.globo.com/').text
    # registra o horário da extração
    hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # localiza as tags de nosso interesse
    bsp_texto = BeautifulSoup(texto_string, 'html.parser')
    # retorna uma lista com cada notícia
    lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
    # imprime quantas notícias foram encontradas
    print("Quantidade de manchetes = ", len(lista_noticias))
    # imprime o conteúdo da primeira notícia
    print(lista_noticias[0].contents)
    lista_noticias[0].contents[1].text.replace('"',"")
    lista_noticias[0].find('a').get('href')
    descricao = lista_noticias[0].contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class': 'bstn-related'})
                # Somente acessará a propriedade
        # descricao = descricao.text if descricao else None text caso tenha encontrado ("find")
    print(descricao)
    metadados = lista_noticias[0].find('div', attrs={'class':'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})
    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None
    print('time_delta = ', time_delta)
    print('seção = ', secao)
    dados = []
    for noticia in lista_noticias:
        manchete = noticia.contents[1].text.replace('"',"")
        link = noticia.find('a').get('href')
        descricao = noticia.contents[2].text
        if not descricao:
            descricao = noticia.find('div', attrs={'class': 'bstn-related'})
            descricao = descricao.text if descricao else None
        metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
        time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
        secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})
        time_delta = time_delta.text if time_delta else None
        secao = secao.text if secao else None
        dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))
    df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
    df.head()

    from datetime import datetime

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    class ExtracaoPortal:
        def __init__(self):
            self.portal = None
        
        def extrair(self, portal):
            self.portal = portal
            texto_string = requests.get('https://globoesporte.globo.com/').text
            hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            bsp_texto = BeautifulSoup(texto_string, 'html.parser')
            lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
            
            dados = []

            for noticia in lista_noticias:
                manchete = noticia.contents[1].text.replace('"',"")
                link = noticia.find('a').get('href')

                descricao = noticia.contents[2].text
                if not descricao:
                    descricao = noticia.find('div', attrs={'class': 'bstn-related'})
                    descricao = descricao.text if descricao else None

                metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
                time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
                secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

                time_delta = time_delta.text if time_delta else None
                secao = secao.text if secao else None

                dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

            df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
            return df

        df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
        df.head()
        # https://medium.com/data-hackers/como-fazer-web-scraping-em-python-23c9d465a37f
