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
#Transformação logaritmica é uma tecnica para ajustar valores discrepantes uniformizando os dados então há alteração dos dados na normalizaçao e
#na padronização não tem alteração de dados
# Já para arrumar valores nulos vc pode remover preencher c moda,media e mediana ou usar tecnicas de imputação avançadas como knn imputer e regressão
#Engenharia de features é o processo de criar novas variáveis a partir das existentes aumentando a precisão e eficácia
#Pode ser com base na frequencia de ocorrencia ou interação entre as variaveis, já a codificação de variaveis categoricas é é transformar dados textuais em números.
#Pode usar para transformar categorica em numero: Onehot encoding, codificação ordinal, codificação em categoria(cat) e label encoding
#One hot encoding usa metodo get dummies para transformar categorias em clunas binarias
#Codificação ordinal mapeia categorias para numeros utilizando um dicionario e a função map
#Codificação com categoria (cat) utiliza o tipo category do pandas para converter valores em números
#Label Encoding utiliza o label encoder da sckit learn para converter valores únicos em numeros
#Padronização Standardscaler media 0 e dp de 1 /Normalização intervalo entre 0 e 1 ou pode ajustar para outros intervlos
#A preparação é limpar, transformar e organizar dados brutos para analise.
#Qual tecnica vc utiliza para tratar discrepancias significativas nos dados de um conjunto de salrios onde alguns valores são extremamente altos em comparação a maioria
#R: Transformação logaritmica pq ela reduz a influencia de valores discrepantes em uma distribuição o que é útil quando há uma grande variação entre valores

#Transformação logaritmica é usada para reduzir a presença de discrepancias extremas em dados numericos ela é especialmente útil quando há uma grande variação entre valores
#já que diminui a variação entre eles

#Boxcox só para dado +, caso contrário tem q add constante essa tecnia ajusta osdados a uma distribuição normal, eliminando altliers e transformando os dados
#p que sigam uma distribuição mais próxima da normalidade
#Codificação onehot é usada para transformar variáeis categoricas em várias colunas binárias onde kd coluna representa uma categoria. Ela é util quando as variaveis categoricas
# não tem uma ordem inerente e podem ser tratadas de forma binária
#Contagem de frequencia: Transforma variáveis categóricas em numeros com base na frequencia de suas ocorrencias. é uma boa opção para atribuir valores numericos a categorias de forma proporcional a sua relevancia no conjunto de dados
#Interação de variaveis cria novas variaveis combinando duas ou mais já existentes. Ela é util para identificar interações entre variaveis que podem não ser evidentes se analisadas separadamente
#Box cox ele normaliza dados, mas exige ajuste caso os dados sejam negativos como a add de constantes
#Min Max normaliza trazendo os valores para uma escala comum mesmo sem uma distribuição normal
#Transformação Logaritmica é a mais adequada para variaveis numericas com grande amplitude de valores
#Contagem de frequencia é útil para dar mais peso as categorias comuns


