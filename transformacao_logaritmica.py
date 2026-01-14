import pandas as pd
import numpy as np
from scipy import stats    #importa as bibliotecas

pd.set_option('display.width', None)          #confiura a tela do terminal
pd.set_option('display.max_columns', None)

#diz qual o banco de dados
df = pd.read_csv('clientes_v2_tratados.csv')

#A transformação logaritmica ajuda na criação de valores equidistantes para as escalas é mais usado
#A transformação logaritmica muda a forma de distribuição não é como normalizar/padronizar
#A transformação logaritmica estabiliza a variancia dp raiz 2 da variancia
# usado quando vc tem mt diferença entre os valores sendo bom p ajustar evitar outlier e evitar erros

#A transformação muda a distribuição dos dados a normalização e padronização não muda a distribuição dos dados
#apenas redimensionam os dados

#ex transformação logaritmica
df['salario_log'] = np.log1p(df['salario'])
print('dps do t log', df.head())


#ex transformação c box-cox, o +1 é p evitar valores negativos
df['salario_boxcox'], _ = stats.boxcox(df['salario'] +1)  #O _ é só uma convenção em phyton q diz, esse valor existe mas eu n vou usar
print('dps do t boxcox', df.head())

#Codificação de frequenc. é mt usada p misturar campos
#ex estado q n é numerico assim quanto mais daqele estado aparecer maior vai ser
#ou seja poderia usar esse exemplo p saber qual estado que tem maior numero de clientes com isso dá para criar módulos
#e ver onde estão concentrados o maior número de clientes

estado_freq = df['estado'].value_counts()/len(df)
#o value count diz a quatidade de estados e dividido pelo numero de linhas
df['estado_freq'] = df['estado'].map(estado_freq)
#o .map pega a equação q vc criou e faz o mapeamento dela atribuindo um numero e colocando em %
print('dps do estado freq', df.head())

#A interação é outra possibilidade de explorar a relação entre os dados aqui ele usa para avaliar a interação entre idade e filhos
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print('dps do idade e filhos', df.head())
#O tratamento de dados é usado para limpar e corrigir os dados
#A preparação dos dados é para transformar e estruturar os dados para fazer uma análise
#Standart Scaler é um méodo para padronização que ajusta os dados para q tenham uma media de 0 e o dp de 1
#O standartScaler para padronização faz parte da biblioteca Scikit-learn

#RobustScaler é um metodo de padronização que reduz o impacto de outlier ajustando os dados p media 0 e dp 1
#One hot-encoding é uma técnica de codificação de variaveis categoricas que transforma cada categoria em
#uma clouna binária que é separada usando o get dummies do pandas

#MinMaxScaler é um metodo de normalização que ajusta os dados para um intervalo entr 0 e 1(pode ser outro)
#Label encoding é uma tecnica de codificação de variaveis categoricas que transforma valores unicos em nmeros inteiros utilizando o
#labelencoder da scikit-learn

#Engenharia de features é o processo de criar novas variaveis (fetaures) a partir das já existentes para melhorar o desempeho dos métodos
#de machine learning Inclui tecnicas como transformação logaritmica criação de features baseada na frequencia da ocorrencia
#e interação entre variáveis

#Antes de qualquer análise é necessário verificar e tratar os dados nulos já que os dados incompletos podem distorcer os resultados
#das analises e modelos estatisticos. Sendo assim, é recomendado usar meodos como a remoção de valores nulos e imputação de valores para esses casos
#É importante também transformar variáveis categoricas em numericas para facilitar a analise e a construção de modelos
#algumas opções para transformar as variaveis categoricas são onehot-encding, codificação ordinal e o label encoding.,

#Padronize e normalize os dados para garantir que todas as variaveis estejam na mesma escala isso é especialmente importante para algoritimos de machine learning que
#que são sensiveis a esala de dados  algumas opções são: StandartScaler, MinMaxScaler e biblioteca Scikit-learn
#Crie novas features a partir das existentes para melhorar o desempenho dos modulos de machine learning algumas tecnicas são as de
#transformação logaritmica e a interação entre as variaveis

#Exemplo 1 usado para previsão de vendas: Empresas de varejo utilizam tecnicas de padronização e normalização para
# ajustar dados historicos de venda permitindo a construção de modelos preditivos mais precisos

#Exemplo 2 usado para analisar os clientes, empresas de marketing utilizam a codificação de variavis categoricas para transformar
#dados demograficos e comportamentais em formatos q podem ser analisados por algoritmos de machine learning.














