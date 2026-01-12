#depois de transformar os dados é preciso preparar para garantir que os modelos estatísticos vão funcionar de forma ótima
#para isso ele já começa criando um banco de dados com mais colunas

import pandas as pd
df = pd.read_csv('clientes-v2.csv')
pd.set_option('display.width', None)

print(df.head().to_string())   #exibe o cabeçalho
print(df.tail().to_string())  #exibe os 5 primeiros e os 5 últimos
df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y',errors='coerce')

print('Verificação inicial')
print(df.info())    #Mostra todas as colunas campos nulos e tipos
print('início da análise', df.isnull().sum()) #vai dar a soma dos valores nulos
#como pode parecer um número muito grande é melhor exibir em porcentagem
print('%dados nulos ', df.isnull().mean()*100, df.dropna(inplace=True)) #mostar quantos % e dps remove tds os dados nulos
print(' verificando se excluiu a %dados nulos ', df.isnull().mean()*100, df.dropna(inplace=True))

print('analises duplicados', df.duplicated().sum())
print('dados unicos', df.nunique()) #campos que podem ser usados p id as pessoas ai tem q ocultar/remover
print('estatisticas', df. describe()) #gera dados estatísticos básicos std é o padrão
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head( ).to_string)
#optou por pegar só esses campos, observe q no primeiro df tem mt mais campos e agr ele exibe só alguns

# optou por salva em um novo arquivo esses dados p usar dps
df.to_csv('clientes_v2_tratados.csv', index=False)



