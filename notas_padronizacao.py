#Pontos de Atenção
import pandas as pd
from numpy.ma.extras import column_stack
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# é importante verificar e tratar valores nulos
data = pd.read_csv('clientes_v2_tratados.csv')
print(data.isnull().sum()) #Mostra quantos valores nulos em kd coluna
data = data.dropna()
print(data.head())

# dps Padronizar e Normalizar
scaler = MinMaxScaler()
data[['idade', 'salario']] = scaler.fit_transform(
    data[['idade', 'salario']]
)
print(data[['idade', 'salario']].head())

#Transformar as variaveis categoricas em numeros:
data = pd.get_dummies(data, columns =['estado'])
print(data.head())

#Realizar análise exploratoria
print(data.describe()) #métodos para obter estatisticas descritivas dos dados
sns.histplot(data['idade'])    #Bibliotecas de exploração para criar gráficos exploratorios
plt.show()

#Faz um grafico c os salarios log
data['log_salario'] = np.log(data['salario'] + 1)
print(data.head())

#Resumão
#é importante transformar e categorizar dados para facilitar a analise e a construçao de modelos de machine learning.
#os dados transformados e categorizados permitem que os algoriimos de machine learning interpretem e processem as informações de maniera
#mais eficaz melhorando a precisão e a eficiencia dos modelos além disso essas transformações ajudam a padrnizar os dados
# o que os torna mais comparaveis e interpretaveis
#A análise exploratoria dos dados auxilia a preparação dos dados pq permite a identificação de padroes,  tendencias e anomalias
#Também ajuda a detectar valores nulos duplicados e unicos além de fornecer insights sobre a distribuição e a relação entre as variaveis
#A EDA é uma etapa crucial para entender a qualidade dos dados e determinar as transformações necessarias para as analises subsequentes
#O robustscaler é uma biblioteca de escalonamento que reduz o impacto dos outliers pq usa medianas e quartis, útil quando tem mt outlier
#pq esses dados mt discrepantes podem distorcer os resultados. O standard(média 0 e dp de 1) sofre mais c isso de mt outlier