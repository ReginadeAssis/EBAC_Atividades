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