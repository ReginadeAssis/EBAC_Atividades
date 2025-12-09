from operator import index
import pandas as pd

#explorando em passos:
#carrega arquivo:

df= pd.read_csv('clientes.csv')

#Mostra as primeiras linhas:
print(df.head())

#Dps a ideia é olhar as linhas e colunas
print(df.shape)
print(df['nome'])
#Vê os tipos de dados e valores nulos:
print(df.info())

#vc tbm pode já remover alguma coluna q tem certeza de n vai usar:
#df = df.drop(columns=['nome_da_coluna'])

#pode padronizar o campos de txto
df['nome'] = df['nome'].str.title()
print(df['nome'])

#Já tratou tbm os valores nulos preenchendo o campo idade com a médiaa das idades da cluna idade
df['idade'] = df['idade'].fillna(df['idade'].mean())

#dá p converter diretao tbm data p formato dta
#df['data']= pd.to_datetime(df['data'])

#p ficar td organizado salva o dataset limpo em um novo csv
df.to_csv('dados_limpos.csv', index=False)

#Já começando e tratando os valores nulos
df = pd.DataFrame({'A': [1,2,None,4]}) #cria um data novo chamado A q recebe 1,2,none e 4 dps preenche o valor nulo none c 0,
#no outro só eleva ao quadrado
df['A'] = df['A'].fillna(0)
df['B'] = df['A'] * 2
print(df['A'])
print(df['B'])

# dá p converter d 1x tbm
df = pd.DataFrame({'date':['2021-01-01','2021-02-01','2021-03-01']})
df['date']= pd.to_datetime(df['date']) #pega sua lista string e passa para o formato data
df['date'] = df['date'] + pd.Timedelta(days=1)#add mais um dia as datas p corrigir
print(df['date'])

#Remover duplicadas:
df= pd.DataFrame({'D': [1,2,2,4]})
df = df.drop_duplicates()
print(df['D'])

#Padronizar campos de texto
df = pd.DataFrame({'nome':['Alice', 'Bob', 'CHARLIE']})
df['name']=df['nome'].str.title()
print(df['name'])































