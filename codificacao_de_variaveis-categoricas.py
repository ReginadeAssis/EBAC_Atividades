#é transformar dados textuais em dados numéricos

import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('clientes_v2_tratados.csv')
print(df.head())

#Abaixo ele usa cdificação one-hot p estado civil assim ele vai criar a coluna estado civil se sim ou n casado\solteiro
#Na vdd p cada alternativa ele vai criar uma coluna que completa c sim ou não

df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix = 'estado_civil')], axis = 1)
print('Depois de one-hot p estado civil', df.head())

#Ele tbm dá o exemplo de ordinal p nível de educaçao
#Cria como se fosse um dicionario:
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Medio':2, 'Ensino Superior':3, 'Pós Graduação':4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
#acima cria coluna no df pega o nivel_educacao do df e mapeia c o .map(mapeia os valores e respostas)
#dps pega e troca o nome pelo valor
print('Após ordinal', df.head())

#como seria mt complicado criar dicionários c os números com mt opção vc pode usar o metodo .cat.codes q cria essas legendas
df['area_atuacao_code'] = df['area_atuacao'].astype('category').cat.codes
#cria o cmpo area de atuação code q recebe os valores do banco de dados de are ade atuação já com o cat codes aplicado

print('Dps de catcode em area de atuacao', df.tail())

#Também dá para usar o label q vai converter kd valor único em um label . Aqui ele usou isso para estado
label_encoder = LabelEncoder()
df['estado_code'] = label_encoder.fit_transform(df['estado'])
print('Data dps de label', df.head())

#de mum modo geral eles usam o nome feature para se referir aos campos no processo a partir de dados já existentes vc vai criar novas features
#com novas variaveis o q melhora o desempenho dos modelos
# A codificação é diferente da transformação na codificação vc pega um texto e transforma ele em um numero
#Na transformação vc transforma os seus dads criando mais e novas informações
