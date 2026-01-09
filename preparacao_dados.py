#depois de transformar os dados é preciso preparar para garantir que os modelos estatísticos vão funcionar de forma ótima
#para isso ele já começa criando um banco de dados com mais colunas

import pandas as pd
df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())   #exibe o cabeçalho
print(df.tail().to_string())  #exibe os 5 primeiros e os 5 últimos
df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y',errors='coerce')

print('Verificação inicial')
print(df.info())    #Mostra todas as colunas campos nulos e tipos
print('início da análise', df.isnull().sum()) #vai dar a soma dos valores nulos
#como pode parecer um número muito grande é melhor exibir em porcentagem
print('%dados nulos ', df.isnull().mean()*100, df.dropna(inplace=True)) #mostar quantos % e dps remove tds os dados nulos
print(' verificando se excluiu a %dados nulos ', df.isnull().mean()*100)
