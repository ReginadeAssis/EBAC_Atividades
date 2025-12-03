import pandas as pd
from scipy import stats
#Como identificar e filtrar outlier
#começa td pedindo p ele ler o arquivo q vc vai usar
df = pd.read_csv('clientes_limpeza.csv')

#vc pode só criar um filtro básico como por exemplo uma pessoa com mais de 99 anos
df_filtro_basico = df [df['idade'] < 100]
print('Filtro básico \n', df_filtro_basico[['nome','idade']])

#tbm dá para fazer usando desvio padrão, a stats é a biblioteca esse zscore vai cacular o desvio padrão da idade e o .drop
# vai removendo os valores nulos para não atrapalhar
Zscores = stats.zscore(df['idade'].dropna())
outliers_z = df [Zscores >=3]
print('Outliers z \n', outliers_z)
#assim na vdd ele criou um campo Zscores que recebe as idades tratadas, mas n precisa fazer isso como rotina
#para rotina basta:
df_zscore = df[(stats.zscore(df['idade'])<3)]
print('Zscore z \n', df_zscore)
#df_zscore é o dataframe stats.zscore é a biblioteca q vc está chamando df idade o campo desejado e 3 o valor q vc quer

#outra alternativa é identificar os outliers dividindo os dados em quadrantes ele chama de identificar com iqr
Q1 = df['idade'].quantile(0.25)
#esse q1 vai então pegar 25% dos dados
Q3 = df['idade'].quantile(0.75)
#esse q3 vai então pegar 75% dos dados
IQR = Q3 - Q1
#fazendo os 75% menos os 25 vc tem algo semelhante a uma média, mas não é media pq vc exclui valores mt grandes e pequenos
#a partir disso vc cria um índice definindo um limite superior e inferior esse 1,5 é o padrao para exploração básica
limite_baixo = Q1 - 1,5 * IQR
limite_alto = Q3 + 1,5 * IQR
print('limites iqr \n', limite_baixo, limite_alto)

#O iqr é uma medida de dispersão que mostra variação de dados em torno da mediana e foca nos 50% do centro dos dados ignorando os extremos
#Dizer iqr = Q! - Q3 significa dizer que a maior parte dos valores estão entre esses dois blocos
#O iqr compara a variabilidade entre diferentes grupos de dados não sofrendo tanto com valores extremos O iqr é usado em análise de dados
#para medir a variação central dos dados e a id dos outliers. No banco que ele usa o limite básico sai -23,5 o que significa que alguém alimentou com uma idade negativa

#Ex:
# ex: 2  4	5	7	8	10	12	15	18
# Q1 5 são 25% da amostra
# Q3 15 são 75% da amostra
# IQR =15-5 =>10 ou seja a maior parte dos dados está entre 5 e 15

#Para saber quais são os outliers pegar tds os números abaixo ou acima do índice que vc criou | é o operador ou

#outliers_iqr = df [(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
#Como vc está trabalhando com idade vc pode definir manualmente o quartil
#limite_baixo = 0
#limite_alto = 100

#Também é possível filtrar direto no campo. Ele usa lambda pq mesmo grande ainda ocupa uma linha só ai nessa
#função para cada não endereço ele escrve inválido e se o campo e não for menor que 3 ele retorna o próprio endereço que chama de x
#O split divide por espaço em bloco
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco Inválido' if len(x.split('\n')) < 3 else x)
print('Qtd', (df['endereco'] == 'Endereco Inválido').sum())

#dps de fazer esse tratamento geral vc vai p campo texto e faz as alterações dentro dele
df['nome'] = df['nome'].apply(lambda x: 'Nome Inválido' if isinstance(x, str) and len(x) > 50 else x)
#Ele aplica essa função na coluna nome add nome inválido se e se (isinstance) se o x for strng e tiver algo digitado e tendo mais de 0 letras
print('Qtd', (df['nome'] == 'Nome Inválido').sum())

#Ai dps vc salva em outro arquiivo csv
df.to_csv('clientes_remove_outliers.csv', index = False)








