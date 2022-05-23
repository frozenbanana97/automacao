import gpxpy
import pandas as pd

gpx_file = open('ler.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
temp = gpx.to_xml()
fulldf = pd.read_xml(temp)
# Drop na primeira linha, esses dados do aplicativo não necessários
fulldf = fulldf.drop(0, axis=0)

print('-----------------------\nOrganização de dados...\n-----------------------')

#Dados manuais que serão repetidos nas colunas
observador = input('Observador? ')
grupo = input('Grupo? ')
tempo = input('Condição do clima? ')
varredura = '.'#input('Número da varredura?')
comportamento = 'Lof'#input('Comportamento?')

cabecalho = ('Individuo','Latitude','Longitude','X','Y','Substrato','Comportamento','Condicao','Varredura','Observador','Grupo','Altitude','Nome','Data','Hora')

# Dataframe com os dados que serão divididos entre outras colunas
df = fulldf[['lat','lon','lat','lon','ele']] 
# Fatiando o dataframe em dataframes separados
# for i in fulldf.colums:
#     globals()['teste'+str(i)]=fulldf

obs_varredura = fulldf['name'].str[19:]
df.insert(0, 'ind',obs_varredura, True)
df.insert(5,'sub','', True)
df.insert(6,'com',comportamento, True)
df.insert(7,'con',tempo, True)
df.insert(8,'var',varredura, True)
df.insert(9,'obs',observador, True)
df.insert(10,'gru',grupo, True)
df.insert(12,'nom','', True)
data_varredura = fulldf['name'].str[0:10]
hora_varredura = fulldf['name'].str[11:19]
df.insert(13,'date',data_varredura,True)
df.insert(14,'time',hora_varredura,True)
df.columns = cabecalho

criar_xlsx = input('Deseja gerar um arquivo *.xlsx? 1-sim\n')
if criar_xlsx == '1':
    df.to_excel('Temporario.xlsx')
    print('A exportação foi bem-sucedida...')

# Testar no futuro, eliminando os cabeçalhos e a coluna numérica
#df.to_clipboard()

#print(df.head(10))
#print(df.tail(10))
#xls = pd.ExcelFile('Temporario.xlsx')
#df1 = pd.read_excel(xls, 'Sheet1')
input('<Finalizar...>')