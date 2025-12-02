
import pandas as pd
#agr aula 2 do modulo-Limpeza de dados

#pd.set_option('display.width', None)
#definiu a opção de display para ajustar e mostrar td coluna p endereço n ficar picado.
#print(df.head())

#vc pode já logo remover os dados que não vai usar
#removendo aqui o campo pais pq td são br
#Faz a leitura  do arquivo
df = pd.read_csv('clientes.csv')
pd.set_option('display.width', None)
print(df.head())
df.drop(labels=['pais'], axis=1, inplace=True) #O axis diz se é coluna ou linha no caso a coluna é 1 e o inplace true é para
#não criar outro dataframe já salva no que está
#lembre q a contagem começa do 0 logo esse label2 na vdd é o 3
df.drop(labels=[2], axis=0, inplace=True)
print(df.head())

#normalizar os campos é verificar os textos e definir um padrão
#primeiro pegou o campo nome
df['nome'] = df['nome'].str.title() #o campo do dataframe recebe o campo do data frame.str(indica alteração de texto)
#.title() é o que deixa tds as primeiras letras em maiusculo
#vc pode misturar como por exemplo td minusculo lower() td maiusculo upper(), mas o ideal é ter um padrão
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()
print(df.head())

#Vc pode converter os numeros direto para inteiro c astype(int)
df['idade'] = df['idade'].astype(int) # o campo idade do dataframe recebe idade com seu valor modificado para inteiro
print('testando', df.head())

#Tem várias maneiras de exibir os registros nulos inclusive opções que já tratam esse valor
print('Valores Nulos' , df.isnull().sum()) #assim ele só dá a coluna e mostra a quantidade de valores nulos em cada uma
#se coloca .sum().sum() ai ele soma td de tds as colunas e mostra um resultado só

#Criou um dataframe para cada uma das opções de remoção de valores nulos
df_fillna = df.fillna(0) #aqui o dataframe fillna substitui tds os valores nulos por zero mas poderia ser qualquer coisa
#Acima ele cria um dta frame q vai receber o dtaframe pai com a função fillna(0) ativa
print('vc retirou então tem q ser 0 a soma de td mesmo', df_fillna.isnull().sum().sum())


#agr ele criou um dataframe para receber os valores já removidos 
df_dropna = df.dropna()
print('Quantidade de valores com drop', df_dropna.isnull().sum().sum()) # Aqui vai ser zero tbm n pq vc substituiu por 0, mas pq n tem nenhum td removido

#Agr ele criou uma lógica de só manter o q tiver o mínimo de caracteres para poder ser
#analisado, já que menos q isso demonstra uma informação incompleta
df_dropna4 = df.dropna(thresh=4) #aqui ele mantém pelo menos 4 valores não nulos
print('Com no mínimo 4', df_dropna4.isnull().sum().sum())

#Agr ele já sabe q tem um campo identificador, o cpf q está incompleto e não vai ser usado dá para já remover o campo
df = df.dropna(subset=['cpf']) #aqui ele colocou direto dentro do df o dataframe df recebe o df com a alteração de cpf
print('Quantidade de registros nulos c cpf',df.isnull().sum().sum()) # ele mostra q tem 22 registros q tem cpf mas q tbm tem 1-3 campos nulos

#Mostrou algumas opções de modificar coluna por coluna p evitar problema
#Nesse exemplo a coluna estado do dataframe já vai td p desconhecido com o inplace true
#e não precisa atribuir ao data frame ele mesmo ele já executa
df.fillna(value={'estado':'Desconhecido'}, inplace= True)
print(df['estado'])

#Aqui ele criou um dataframe novo chamdo endereço que recebe ele mesmo só q agr é endereço não informado
df['endereco'] = df['endereco'].fillna('Endereço não informado')

# Aqui ele cria a coluna idade corrigida como sendo o campo idade preenchido com a média das idades do banco de dados quando não tem nenhum valor no campo idade
df['idade_corrigida'] = df['idade'].fillna(df['idade'].median())

#Como tratar as datas-cria a coluna data corrigida que é a coluna data com formato de data e c erro tratado

df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #se der erro ele gera um valor nulo

##O tratamento de valores duplicados é feito depois pq pode ter dado nulo ou com formatação diferente

print('qnt de registros atual', df.shape[0])

#remove duplicadas
df.drop_duplicates(subset='cpf', inplace=True)

print('Dados limpos\n', df) #\n é o espaço

#vc cria as colunas p corrigir os dados, mas só dps de ver se está td certo é que vc transfere de volta para a coluna mãe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

#Como vc n vai usar td vc cria um dataframe com o que vai usar, só as colunas que vc quer
df_salvar = df[['nome','cpf', 'idade', 'data', 'endereco','estado']]
df_salvar.to_csv('clientes_limpeza.csv', index= False)
#to_csv salva como csv o index false para não gerar a coluna de index que tem 0 e 1
print('Novo excel \n', pd.read_csv('clientes_limpeza.csv'))











