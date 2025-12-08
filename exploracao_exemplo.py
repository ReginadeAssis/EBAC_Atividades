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
df['data']= pd.to_datetime(df['data'])

#p ficar td organizado salva o dataset limpo em um novo csv
df.to_csv('dados_limpos.csv', index=False)

