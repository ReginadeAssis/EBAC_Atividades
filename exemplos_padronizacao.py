import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
#aqui ele importa as classes para padronização e #normalização dos dados

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#ex de DataFrames
data = {'idade':[25,45,35,50],
		'salario':[50000,100000,75000,120000]
		}
df = pd.DataFrame(data) # aqui ele converte o dicionario em um dataframe do pandas

#Padronização
scaler = StandardScaler() #inicializa o objeto standartScaler
df['idade_padronizada'] = scaler.fit_transform(df[['idade']]) #o fit transform apliaca a padronização na coluna idade
df['salario_padronizado'] = scaler.fit_transform(df[['salario']])

#Normalização
min_mx = MinMaxScaler()
df['idade_normalizada'] = min_mx.fit_transform(df[['idade']])
df['salario_normalizado'] = min_mx.fit_transform(df[['salario']])

print(df)

