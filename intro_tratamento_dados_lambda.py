import pandas as pd

#Faz a leitura  do arquivo
df = pd.read_csv('clientes.csv')

print(df.head().to_string())
#o df head exibe os primeiros registros do data frame e o to_string põe em uma linha só

print(df.tail().to_string())
# o tail aqui age para pegar o final, a "cauda"

print('Qtd' , df.shape)
#vai mostrar quantas linhas e colunas

print('tipagem:\n', df.dtypes)
#vai mostrar seus tipos de dados

print('Valores nulos:\n' , df.isnull().sum())
#mostra os valores nulos. \n dá espaço- a , concatena-o isnull faz uma busca em td o banco de dados ai n dá p ver td
# o .sum soma e mostra por coluna

#A expressão lamba é uma forma de escrever uma fnção em uma linha
#Abaixo função que vai p lambda-o def é o q cria a função

def eleva_cubo(x):
	return x ** 3

#parar fazer lambda vc cria uma variável e atribui a função a ela
eleva_cubo_lambda = lambda X: X ** 3

#Mostra o resultado das 2 elevando o 2
print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'números': [ 1,2,3,4,5,10]})
df['cubo_função'] = df['números'].apply(eleva_cubo)
df['cubo_com_lambda'] = df['números'].apply(eleva_cubo_lambda) #atribuindo a variável como função, mas n faz sentido pq
#cria mais uma linha o q poderia ser uma função
df['cubo_com_lambda2'] = df['números'].apply(lambda x: x ** 3)

print(df)



















