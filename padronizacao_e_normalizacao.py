#Para fazer esse processo usa a biblioteca sklearn, o que vem dps do import são os módulos que ele vai usar
#Como exemplo ele trouxe pegar os dados entre 0 e 1 e normalizar os dados nesse intervalo, isso é ipc
#para comparar as variáveis pq em escalas mt grandes fic impossível
import labels
import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

pd.set_option('display.width', None) #faz aquela pequena config para mostrar no terminal
pd.set_option('display.max_columns', None)

#pede p ler os dados criando o novo dataframe
df = pd.read_csv('clientes_v2_tratados.csv')

print(df.head()) #p ele exibir o começo

#ele deleta todos os campos pq vai analisar só idade e salário
#poderia ser: df=df[['idade','salario']]
df= df.drop(labels=['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil','area_atuacao'], axis=1)

print(df.head())
#para normalização ele usa minmaxscaler onde vc cria variável igual ao modulo e o phyton já no automático normaliza como 0 e 1 para mudar o padrão
#ai já é o segundo exemplo

#Usando o scaler para normalizar ele altera a escala e puxa td p 0 e 1
#primeiro ele cria a variável para receber o módulo
scaler = MinMaxScaler()

#cria campo novo para receber os dados normalizados
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])

df['salario_MinMaxScaler'] = scaler.fit_transform(df[['salario']])

#vc pode n querer usar 0 e 1 dai muda add a feature range: scaler = MinMaxScaler(-1,1) como no exemplo abaixo onde
#foram criadas novas colunas para receber os dados normalizados no novo intervalo
novo_intervalo = MinMaxScaler(feature_range =(-1,1))
df['novo_intervalo_idade'] = scaler.fit_transform(df[['idade']])
df['novo_intervalo_salario'] = scaler.fit_transform(df[['salario']])

#A normalização vai tratar do intervalo, já a padronização é média 0 e dp =1
#O scaler altera a escala e normaliza entre 0 e 1- ele altera a escala

scaler = StandardScaler()
#precisa criar uma variavel para receber esse modulo
#cria um campo novo para receber os dados normalizados e não alterar a coluna idade
df['idade_Standart_Scaler'] = scaler.fit_transform(df[['idade']])
print(df.head())

#Já o robust scaler é melhor quando vc tem mts dados discrepantes para remover outliers
#Robust usa mediana e qr o scaler usa media e dp
scaler = RobustScaler()
df['idade_RobustScaler'] = scaler.fit_transform(df[['idade']])
df['salario_RobustScaler'] = scaler.fit_transform(df[['salario']])
print(df.head(15))

#ex mean salario: 0,16 esse valor está mais perto de 0 do qe do 1;logo tem poucos salários altos e muitos salarios baixos
#mean -0,06 usa 0 e 1 p trabalhar a distancia entre numeros 0.062 ainda é mais perto de zero
# A mediana na normalização exclui o q e mt baixo e mt alto no robust scaler os intervalos são menores pq remove outliers

#Agr para marcar as saídas formatadas:
print("Idade-Min:{:.4f} Max:{:.4f} Mean:{:4f} Std:{:.4f}".format(  #esse .format é o mode de exibir q vai usar o q vc pediu
	df['idadeMinMaxScaler'].min(),
	df['idadeMinMaxScaler'].max(),
    df['idadeMinMaxScaler'].mean(),
	df['idadeMinMaxScaler'].std()
))
#Min{:.4f} é para idadeMinMaxScaler.min() com 4 casas decimais e float, poderia ser int, +,-....

#Agr print o min maxscaler de 0-1
print('idade-Min:{:.4f} Max:{:.4f} Mean:{:.4f} Std:{:.4f}'.format(
	df['novo_intervalo_idade'].min(),
	df['novo_intervalo_idade'].max(),
	df['novo_intervalo_idade'].mean(),
	df['novo_intervalo_idade'].std()
))

print('salario-Min:{:.4f}, Max:{:.4f} Mean:{:.4f} Std:{:.4f}'.format(
	df['novo_intervalo_salario'].min(),
	df['novo_intervalo_salario'].max(),
	df['novo_intervalo_salario'].mean(),
	df['novo_intervalo_salario'].std()

))

print("\n MinMaxScaler de -1 a 1:")
print('idade-Min:{:.4f} Max:{:.4f} Mean:{:.4f} Std:{:.4f}'.format(
	df['idadeMinMaxScaler'].min(),
	df['idadeMinMaxScaler'].max(),
	df['idadeMinMaxScaler'].mean(),
	df['idadeMinMaxScaler'].std()
))

print("salario-Min:{:.4f} Max:{:.4f} Mean:{:.4f} Std:{:.4f}".format(
	df['salario_MinMaxScaler'].min(),
	df['salario_MinMaxScaler'].max(),
	df['salario_MinMaxScaler'].mean(),
	df['salario_MinMaxScaler'].std()
))

print("\n StandartScaler q a media para 0 e o dp para 1")

print('idade-Min:{:.4f} Max:{:.4f} Mean:{:.4f} std:{:.4f}'.format(
	df['idade_Standart_Scaler'].min(),
    df['idade_Standart_Scaler'].max(),
	df['idade_Standart_Scaler'].mean(),
	df['idade_Standart_Scaler'].std()
))

print('salario- Min:{:.4f} Max:{:.4f} Mean:{:.4f} std:{:.4f}'.format(
	df['salario_RobustScaler'].min(),
	df['salario_RobustScaler'].max(),
	df['salario_RobustScaler'].mean(),
	df['salario_RobustScaler'].std()
))

#Normalização x Paronização
#Duas técnicas c objetivo igual de redimesionar os dados, ele não troca os dados ele só muda a escala dos dados
#Normalização desloca os valores p q fiquem entre 0 e 1 usando escala MinMax, coloca os dados nesse intervalo p poder comparar
#Padronização vc tira da média e divide pelo dp ai a média fica 0 e o dp =1, vc deixa tds os dados dados na mesma escala c média 0 e dp de 1
#o que não significa q vão estar no mesmo intervalo 0 e 1 por isso é outro método


