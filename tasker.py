import time as tm
import datetime
import os
import calendar
import pandas as pd

class atividade():

    def __init__(self, codigo, data, hora, descricao, atividade, tipo):
        self.codigo = codigo
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.atividade = atividade
        self.tipo = tipo

    def __padronizar_registro(self, string):
        return True

    def __padronizar_hora(self):
        pass

    def __padronizar_data(self):
        pass

    def __alterar_tamanho_coluna(self, arquivo_entrada, arquivo_saida):
        '''
        Método paliativo
        '''
        temp = pd.read_csv(arquivo_entrada)
        # Corrigir o erro do ID, se essa coluna for concatenada, acaba dobrando a coluna _id
        s1 = temp['_id']
        s2 = temp['data']
        s3 = temp['hora']
        s4 = temp['obs']
        s5 = temp['tipo']
        s6 = temp['atividade']
        for i in range(len(s4)):
            # Devolve para a série, somente os primeiros 60 caracteres
            s4[i] = s4[i][:60]
            # Devolve para a série, somente os primeiros 50 caracteres
            s5[i] = s5[i][:50]
        df = pd.concat([s2, s3, s4, s5, s6], axis=1)
        # 
        df.to_csv(arquivo_saida)

class Utilidades():

    def substituir_caracter(self, _texto):
        # importa o método necessário
        from re import sub
        # converte para minúsculo para facilitar as substituições
        _texto = _texto.lower()
        # substitui as letras não permitidas
        novo_texto = sub('[àáâãä]', 'a', _texto)
        novo_texto = sub('[èéêë]', 'e', novo_texto)
        novo_texto = sub('[ìíîï]', 'i', novo_texto)
        novo_texto = sub('[òóôõö]', 'o', novo_texto)
        novo_texto = sub('[ùúûü]', 'u', novo_texto)
        novo_texto = sub('[ç]', 'c', novo_texto)
        # substitui os caracteres não permitidos
        novo_texto = sub('[;,#|_"ºª]²³', '.', novo_texto)
        # retorna o texto corrigido de acordo com o padrão do script
        # input(novo_texto)
        return novo_texto

    def __init__(self, _arquivo="saidas.tasker"):
        '''
        Constructor da classe que já cria uma lista na memória
        [1º parâmetro] por padrão abre o arquivo padrão do programa
        '''
        # Lista temporária, depois de encontrar outra solução, não utilizar mais esse atributo
        self.lista = self.visualizar_arquivo(_arquivo)
        # Popula o DF que será utilizado na manipulação dos dados
        self.df = pd.read_csv(_arquivo)
        

    def visualizar_arquivo(self, filename):
        '''
        Método para visualizar os dados fazendo varredura linha a linha
        - Precisa atualizar para uma maneira mais inteligente
        '''
        # Estrutura de dados
        # _id = 5
        # data = 10
        # hora = 5
        # obs = 56 (sem limite, só para mostrar na tela usa-se essa quantidade)
        # nome = 26 (sem limite, só para mostrar na tela usa-se essa quantidade)
        # atividade = 4
        with open(filename) as arquivo:#, 'r', encoding='UTF-8'
            _lista = []

            while (linha := arquivo.readline().rstrip()):
                lst = linha.split(',')
                # se o _id tiver menos de 5 caracteres, manipulará para padronizar
                # _id
                if len(lst[0]) < 5:
                    txt = ''
                    # Adiciona espaços de descontando 5 do tamanho do _id
                    for i in range(5 - len(lst[0])):
                        txt += ' '
                    lst[0] = lst[0] + txt
                # obs
                if len(lst[3]) > 55:
                    lst[3] = lst[3][0:52]+'...'
                else:
                    txt = ''
                    for i in range(55 - len(lst[3])):
                        txt += ' '
                    lst[3] = lst[3] + txt
                # nome
                if len(lst[4]) > 26:
                    lst[4] = lst[4][0:23]+'...'
                else:
                    txt = ''
                    for i in range(26 - len(lst[4])):
                        txt += ' '
                    lst[4] = lst[4] + txt
                _lista.append(lst)
            # cabeçalho
            _lista[0][1] = _lista[0][1] +'      '
            _lista[0][2] = _lista[0][2] +' '
        return _lista
        
    def visualizar_ultimos(self, lista):
        pass

    def imprimir_arquivo(self, lista, tudo=False):
        '''
        Imprime a lista da memória em um formato de grade
        [1º parâmetro] lista com cinco colunas com os valores a serem impressos
        [2º parâmetro] Se for True (padrão) mostra todos os dados, caso contrário somente os últimos 25 registros
        '''
        top = '╔'+('═'*7)+'╦'+('═'*12)+'╦'+('═'*7)+'╦'+('═'*57)+'╦'+('═'*28)+'╦'+('═'*6)+'╗'
        bot = '╚'+('═'*7)+'╩'+('═'*12)+'╩'+('═'*7)+'╩'+('═'*57)+'╩'+('═'*28)+'╩'+('═'*6)+'╝'
        print(top)
        print('║ '+lista[0][0]+' ║ '+ lista[0][1]+' ║ '+ lista[0][2] +' ║ '+ lista[0][3] +' ║ '+ lista[0][4] +' ║ '+ lista[0][5] +' ║')
        print(bot)
        print(top)
        # número inicial de itens a serem mostrados
        quantidade = 1
        if tudo == False:
            quantidade = len(self.lista) - 25
        for lin in range(quantidade,len(self.lista)):
            texto = '║ '
            # Número de colunas que serão impressas
            for col in range(6):
                texto = texto + lista[lin][col] + ' ║ '
            print(texto)
        print(bot)
        input('<enter>')

    def ler_arquivo(self, filename):
        '''
        Abre um arquivo, lê ele e o transforma de linha em linha do padrão csv, para uma lista na memória
        [1º parâmetro] endereço do arquivo a ser trabalhado
        '''
        with open(filename) as arquivo:#, 'r', encoding='UTF-8'
            lista = []
            while (linha := arquivo.readline().rstrip()):
                lista.append(linha.split(','))
        return lista

    def data_hoje(self):
        '''
        Retorna a data em formato string DD/MM/AAAA
        '''
        data = datetime.datetime.now()
        ano = str(data)[0:4]
        mes = str(data)[5:7]
        dia = str(data)[8:10]
        return dia + '/' + mes + '/' + ano

    def hora_agora(self):
        '''
        Retorna a hora do momento em formato string hh:mm
        '''
        hora = datetime.datetime.now().time()
        hora = str(hora)[0:5]
        return hora

    def ler_senha(self):
        '''
        Método retorna a leitura de um input com a senha digitada
        '''
        import getpass
        return getpass.getpass('Digite sua senha: ')

    def converter_csv_json(_arq_csv, _arq_json, _chave_principal, _encoding):
        ''' 
        Método utilizado para transformar um arquivo CSV para JSON.
        [1º parâmetro] nome do arquivo csv
        [2º parâmetro] nome do arquivo json
        [3º parâmetro] a coluna principal do csv que será transformada em chave única
        [4º parâmetro] o encoding que será utilizado parâmetro (utf-8, ansi, latin-1, etc)
        '''
        # Import
        import csv
        import json
        # Cria um dicionário
        dicionario = {}
        # Abre o arquivo csv
        with open(_arq_csv, encoding=_encoding) as csvf:
            # Recupera a informação
            arquivo = csv.DictReader(csvf)
            # Converte cada linha adicionando-as para dentro do dicionário
            for linhas in arquivo:
                # Adiciona a chave
                chave = linhas[_chave_principal]
                # Criando para o dicionário
                dicionario[chave] = linhas
        # Cria um arquivo com o nome passado como parâmetro e o escreve com o método da biblioteca
        with open(_arq_json, 'w', encoding=_encoding) as jsonf:
            # Utiliza a indentação de 2
            jsonf.write(json.dumps(dicionario, indent=2))

    def para_json(array):
        '''
        Método utilizado para transformar em um arquivo JSON
        '''
        import json

        a = {
            'name':'Max',
            'age':22,
            'marks':[90,50,80,40],
            'pass':True,
            'object':{
                'color':('red','blue')
            }
        }
        with open('teste.json', 'w') as fh:
            fh.write(json.dumps(a))
            
        print(json.dumps(a, indent=2, separators=('.',' = '), sort_keys=True))

    def calendario(self):
        '''
        Método printa um calendário na tela, utilizando o mês corrente do SO
        '''
        # recupera a data local (SO)
        _data = tm.localtime()
        # recupera o ano
        _year = _data[0]
        # recupera o mês
        _month = _data[1]
        # faz a impressão na tela do calendário
        print(calendar.month(_year, _month))
        input('<enter>')

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

    def limpa_tela(self):
        '''
        Método para limpar a tela do terminal
        '''
        import os
        os.system('cls')

    def menu(self, textos, cabecalho=''):
        '''
        Método para imprimir um menu na tela
        '''
        # chama o método interno para limpar a tela
        self.limpa_tela()
        # Ponta superior esquerda do menu
        pse = '╔'
        # Ponta superior direita do menu
        psd = '╗'
        # Ponta inferior esquerda do menu
        pie = '╚'
        # Ponta superior direita do menu
        pid = '╝'
        # Reta do menu
        ret = '═'
        # Lateral do menu
        lat = '║'
        # procura a maior string no array
        maior = 0
        # percorre todo o array do parâmetro
        for item in textos:
            if len(item) > maior:
                # pega a string com a maior quantidade
                maior = len(item)
        # multiplica o caracter de reta pelo tamanho da maior string + 2 
        ret *= maior + 2
        # imprime a parte de cima do menu
        print(f'{pse}{ret}{psd}')
        # se tiver cabeçalho no menu
        if cabecalho != '':
            # cabeçalho esquerdo
            cae = '╠'
            # cabeçalho direito
            cad = '╣'
            # divide o valor por dois, e trunca para dividir o cabeçalho no menu
            espacos = ' ' * int((maior - len(cabecalho))/2)
            # ajusta o cabeçalho no topo do menu
            # if len(cabecalho) > 1:
            #     print(f'{lat} {espacos}{cabecalho}{espacos} {lat}')
            # else:
            #     # Se for somente um caracter, precisa descontar um caracter para ajustar corretamente
            print(f'{lat} {espacos}{cabecalho}{espacos} {lat}')
            # imprime a parte final do cabeçalho
            print(f'{cae}{ret}{cad}')
        for texto in textos:
            # retira o <enter> que possa existir na string, que desconfigurará o menu
            texto = texto.replace('\n', '')
            # recupera o tamanho da string
            espacos = ' ' * (maior - len(texto))
            # para todas as strings de parâmetro imprime no menu
            print(f'{lat} {texto}{espacos} {lat}')
        # imprime a parte de baixo do menu
        print(f'{pie}{ret}{pid}') 

    def padronizar_numero(self, numero):
        '''
        Devolve um número de dois dígitos, completa com zero no primeiro se precisar
        [1º parâmetro] número que se deseja padronizar
        '''
        texto = str('{:02d}'.format(numero))
        return texto

    def finalizar(self, vInicial=0, vFinal=3, tempo_espera=2):
        '''
        Cria a animação de saída do programa
        primeiro e segundos parâmetros são utilizados no cronômetro de tempo e para a animação
        terceiro parâmetro é utilizado para segurar a mensagem final do script!
        '''
        # Variável para controlar os três estágios da animação
        i = 0
        while vFinal > vInicial:
            if i == 0:
                msg = '≤≤≤≤≤≤'
            elif i == 1:
                msg = '≡≡≡≡≡≡'
            else:
                msg = '≥≥≥≥≥≥'
                i = -1
            i += 1
            os.system('cls')
            print('Finalizando ', msg)
            vInicial += 1
        os.system('cls')
        print('Obrigado por usar nosso script!\nTNT Solutions ©® 2021.\n')
        # Espera 'x' segundos para efetivar a saída
        tm.sleep(tempo_espera)

    def linhas_arquivo(self):
        '''
        Retorna o número de linhas do arquivo de dados, o retorno pode ser utilizado
        como chave primária
        '''
        try:
            nLinhas = 0
            with open("saidas.tasker") as arqTemp:
                nl = arqTemp.readlines()
                for g in nl:
                    nLinhas += 1
                return nLinhas
        except:
            input('Arquivos não encontrados!\nentradas.tasker | saidas.tasker')

    def dicionario_dados(self):
        '''
        Transforma a base em um dicionário
        '''
        dic = {}
        arquivo = open("saidas.tasker", "r")
        linhas = arquivo.readlines()
        i = 0
        for g in linhas:
            tupla = linhas[i].split(';')
            dic = { 'codigo':tupla[0],'data':tupla[1],'hora':tupla[2],'obs':tupla[3],'descricao':tupla[4]}
            i += 1
        arquivo.close()
        return dic

    def get_database(self, nomeDB):
        '''
        Retorna uma base de dados do MongoDB
        [1º parâmetro] nome do banco
        '''
        from pymongo import MongoClient
        import pymongo
        # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
        # Lê um arquivo com as informações, para conexão no banco de dados Mongo
        with open('conexao') as arquivoTemporario:
            nl = arquivoTemporario.readlines()
        CONNECTION_STRING = nl[0]
        # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)
        # Cria o banco de dados.
        return client[nomeDB]
    
    def get_colecao(self, _banco, _tabela):
        '''
        Retorna uma coleção do MongoDB
        [1º parâmetro] nome do banco
        [2º parâmetro] nome da tabela
        '''
        # busca o banco de dados
        _dbname = self.get_database(_banco)
        # o parâmetro do método, específica a coleção que será utilizada
        _collection_name = _dbname[_tabela]
        # o método retorna uma coleção inteira, muita atenção quando ela for muito grande
        return _collection_name.find()

    def insert_linha(self):
        # Index: {numeroLinhasDoArquivo()}
        # Data: {util.padronizar_numero(data[2])}
        # {padronizaNumero(data[1])}
        # {data[0]};{
        # Hora: padronizaNumero(data[3])}
        # :{padronizaNumero(data[4])}
        # Observação: obs
        # Está ativo?: ativo
        return 'OK!'

    def arquivo_pandas(self):
        '''
        Retorna toda a base utilizando pandas e o arquivo loval
        '''

        try:
            local = pd.read_csv('saidas.tasker')
            print(local)
            input('<enter>')
        except FileNotFoundError:
            input('Arquivos não encontrados!\nentradas.tasker | saidas.tasker')

    def retorna_tudo(self):
        '''
        Retorna toda a base, utilizando o modo de leitura primitivo do Python
        '''
        try:
            with open("saidas.tasker") as saidas:
                tLog = saidas.readlines()
                os.system('cls')
                tempArq = ''
                for g in tLog:
                    tempArq += g
                print(tempArq)
                input('<enter>')

        except:
            input('Arquivos não encontrados!\nentradas.tasker | saidas.tasker')
    
    def atividades_dia(self, _df, _coluna):
        '''
        Retorna a quantidade de atividades por dia
        [1º parâmetro] Data Frame a ser manipulado
        [2º parâmetro] Coluna do Data Frame a ser agrupada
        '''
        return _df.groupby([_coluna]).count()

    def menu_manipulacao(self, _df):
        '''
        Chama o menu para manipulação dos dados armazenados
        '''
        opcoes = ['1- Hoje','2- Por data','3- Por atividade']
        self.menu(opcoes,'Filtros ')
        df = _df
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            _data = self.data_hoje()
            dfm = df.loc[(df['data'] == _data)]
            dfm = dfm[['ati.','obs']]
            print(dfm)
            input('<enter>')
        elif opcao == '2':
            _data = input('Digite a data (DD/MM/AAAA) desejada: ')
            dfm = df.loc[(df['data'] == _data)]
            dfm = dfm[['ati.','obs']]
            print(dfm)
            input('<enter>')
        elif opcao == '3':
            dfm = df['ati.'].unique()
            print(dfm)
            input('<enter>')
        else:
            print(df)
        input('<enter>')

    

    
########### Início do programa ############################################################################
try:
    # variável de controle do fluxo
    f = True
    # cria um objeto da classe Utilidades
    util = Utilidades()
    # conectar = 'n'#input('Conectar mongoDB? s=sim\n')
    # if conectar == 's':
    #     colecao = util.get_colecao('Base','Tasker')
    #     dfLocal = pd.DataFrame(list(colecao))
    # 
    tupla = ()
    # acessa o arquivo, para montagem do menu
    with open("entradas.tasker") as file_object:
        # le todas as linhas
        lista = file_object.readlines()
    # variável usada para inserir observações
    obs = '' 
    # percorre a lista alterando ela, de 0 até o tamanho dela
    # passa o conteúdo da lista para tupla
    temp = ''
    for i in range(len(lista)):
        # retirando o caracter <enter> da string
        texto = lista[i].replace('\n', '')
        # a variável está sendo completada
        temp = temp + texto + '|'
        # reconfigura a lista de arquivos, para mostrar no menu
        lista[i] = (str(i) + '-' + lista[i])
    # a tupla recebe a string fatiada, para ser utilizado como 
    tupla = temp.split('|')
    dfLocal = util.df
    while f == True:
        try:
            # montagem do menu do programa na tela
            util.menu(lista,'Tasker  ')
            print('t=todas as entradas | c=calendário | m=manipulações | x=xp | u.d\n')
            entrada = input('Digite a opção desejada!\n')
            if entrada == 't':
                # atualiza a lista da classe, que guarda todas as informações
                # imprime todas as entradas registradas
                dft = pd.read_csv('saidas.tasker')
                print(dft)
                input('<enter>')
                # util.imprimir_arquivo(util.visualizar_arquivo("saidas.tasker"))
            elif entrada == 'c':
                # imprime o calendário do mês corrente na tela
                util.calendario()
            elif entrada == 'm':
                # imprime todas as entradas registradas = com pandas
                print(dfLocal)
                util.menu_manipulacao(dfLocal)
            elif entrada == 'x':
                dfm = util.atividades_dia(dfLocal,'data')
                # quantidade de dias
                print(f"Número de dias: {dfLocal['data'].nunique()}")
                # número de atividades por dia
                # ordenar por data?
                print(dfm['ati.'])
                input('<enter>')
            elif entrada.isdigit() and int(entrada) < len(lista):
                # recupera a data e hora do momento
                datahora = util.data_hoje() + ',' + util.hora_agora()
                # busca o índice único, varrendo o arquivo e contando o número de linhas -MELHORAR
                indice = util.linhas_arquivo()
                # adiciona a variável, o texto da atividade
                atividade = tupla[int(entrada)]
                # fatia a atividade, para dividir nome da atividade, terei que melhorar esse método
                tupla_temp = atividade.split(',')
                atividade = tupla_temp[0]
                # se encontrar a cadeia '...' dá a alternativa de personalizar a atividade
                if atividade.find('...') >= 0:
                    # substitui pelo novo valor informado
                    atividade = atividade.replace('...', input(f'[ {atividade} ] Digite o complemento: '))
                atividade = util.substituir_caracter(atividade) +','+ tupla_temp[1]
                # solicita uma observação
                obs = input('Digite uma observação, ou deixe em branco!\n')
                # método para utilizar apenas caracteres autorizados
                obs = util.substituir_caracter(obs)
                # concatena a observação nas informações anteriormente setadas
                registro = (str(indice) +','+ datahora +','+ obs +','+ atividade + '\n')
                print(registro,'... ok')
                with open('saidas.tasker', 'a') as file_object:
                    # escreve no arquivo
                    file_object.write(registro)
            elif entrada == 'u' or entrada == 'U':
                dft = pd.read_csv('saidas.tasker')
                print(dft.tail(25))
                input('<enter>')
            elif entrada == 'h':
                dft = pd.read_csv('saidas.tasker')
                _data = util.data_hoje()
                dft = dft.loc[dft['data'] == _data, ['nome','ati.','obs']]
                print(dft)
                input('<enter>')
            elif entrada == 'a':
                input('<enter>\nDesabilitado temporariamente...')
            else:
                util.finalizar(0,3,1)
                f = False

        except:
            util.finalizar(0,3)
            f = False

except FileNotFoundError:
    input('Arquivos não encontrados!\nentradas.tasker | saidas.tasker')
    f = False