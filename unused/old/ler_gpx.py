import gpxpy
import pandas as pd

gpx_file = open('ler.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
temp = gpx.to_xml()
fulldf = pd.read_xml(temp)
# Drop na primeira linha, dados do aplicativo não necessários
fulldf = fulldf.drop(0, axis=0)

#Dados manuais repetidos
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
df.to_excel('Temporario.xlsx')

pd.to_clipboard()
# print(df)
#print(df.head(10))
#print(df.tail(10))
input('<Finalizado com sucesso!>')