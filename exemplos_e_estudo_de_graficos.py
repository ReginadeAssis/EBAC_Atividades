import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv('clientes_v3_preparado.csv')

#Abaixo ele pede para fazer a correlação de todos esses campos
df.corr =df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod','area_atuacao_cod','estado_cod']].corr()
#Dps pega isso e joga no gráfico abaixo para fazer mapa de calor da correlação entre as variáveis
sns.heatmap(df.corr, annot=True, fmt=".2f") #chama as variaveis acima e determina formato de exibição
plt.title('Mapa de Calor da correlação entre as variáveis')
plt.show()

#Com esse gráfico dá para ver que estado cod, n de filhos, não precisa usar pq são colunas em branco, a área de atuação tbm tem valor mt baixo pq mostra uma correlação mt fraca
#Faz contagem para estado civil e agrupamento
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

#Agr countplot com legenda e agrupamento
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df) #(campo q ele quer ver, variável q vai agrupar e de onde vem)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
plt.show()

#Conceitos importantes
#Seaborn é uma biblioteca de visualização de dados em phyton que é construida sobre o matplotlib ela oferece uma interface de alto nível para
#a criação de gráficos estatísticos atraentes e informativos
#Pairplot é uma combinação de gráficos de dispersão e histograma a visualização da relação entre multiplas variáveis em um único gráfico sendo útil para explorar a relação ente os dados
#Mapas de Calor são visualizações que utilizam cores para representar a interface de valores em uma matriz de dados eles são eficazes para identificar padrões e correlações em
#um determinado conjunto de dados.
#Histograma representa a distribuição em um conjunto de dados mostrando a frequencia de valores em intervalos específicos sendo útil para entender a distribuição e a
#dispersão dos dados
#graficos de regressão são os graficos que mostram a relação entre variáveis ajudando a visualizar padrões e tendências. São mt usados p prever valores e id correlações
#Graficos de densidade são visualizações que suavizam os dados para criar uma representação contínua e esteticamente agradável da distribuição dos dados.
#Os gráficos de densidade são úteis para identificar padrões e tendências nos dados

#Resumão:
#É fundamental selecionar o tipo de gráfico que melhor representa os dados e a msg que deseja transmitir. por exemplo os gráficos de barra são ideais para
#comparação enquanto gráficos de dispersão são melhores para visualizar correlações
#Aproveite bibliotecas como o matplotlib e seaborne para criar visualizações avançadas. O matplotlib é excelente para gráficos básicos, enquanto o seaborn oferece
#funcionalidades adicionais para gráficos mais complexos e esteticamente mais agradáveis
#Antes de ciar gráficos é importante explorar e entender os dados.Isso inclui verificar a distribuição, identificar outliers e entender as relações entre as variaveis
#Como exemplo para a análise de vendas as empresas utilizam graficos de barra e de pizza para visualizar a performance de venda or produto região ou período e desenvolver estratégias
#Também pode ser usado para a pesquisa de mercado com gráficos de dispersão e de correlação que são usados para analisar a relação entre diferentes variáveis como o preço e satisfação do cliente
#gerando informações importantes para a equipe de marketing

#agr ele dá mais exemplo com os dados no dicionário abaixo
data = {
	'idade':[23,45,56,25,34,42,67,29,38,50],
	'salario':[50000,80000,120000,45000,60000,75000,130000,48000,70000,90000]
}
df=pd.DataFrame(data)

#Gráfico de dispersão com Matplot
plt.scatter(df['idade'],df['salario'],color='blue',alpha=0.5) #(campos, cor e transparecia)
plt.title('Relação entre idade e salário')
plt.xlabel('idade')
plt.ylabel('salario')
plt.show()

#Gráfico de dispersão com seaborn
sns.scatterplot(x='idade',y='salario',data=df,hue='idade', palette='viridis')#(campos, origem, agrupa por idade, cores)
plt.title('Relação entre idade e salário')
plt.xlabel('idade')
plt.ylabel('salario')
plt.show()

#Aqui ele dá exemplo no matplot salvando dps
data = [1,2,3,4,5]
plt.figure(figsize=(10,5)) #ipca determinar o tamanho p salvar p n ficar distorcido
plt.plot(data)
plt.title('Exemplo de salvamento')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.savefig('exemplo.png')
plt.show()

#pq os gráficos são importantes? para transformar dados complexos em visões simples e intuitivas facilitando a identificação de padrões e tendências.
#como salvar um gráfico? plt.savefig(nome do arquivo)
#graficos de densidade são usados para suavizar dados e visualizar a distribuição continua de uma variavel, em seaborn vc pode criar graficos de densidade
#usando o metodo sns.kdeplot que permite ajustar a visualização
#Os gráficos de barra e de pizza com o matplot vc pode usar plt.bar ou dataframe.plot.bar(). Já para os graficos de pizza usa o plt.pie configurando rótulos e ângulos
#o q é pairplot e como ele é util? é uma visualização que combina vários gráficos como de dispersão e histograma para mostrar as relações entre multiplas variaveis numericas, vc cria
#vc cria com sns.pairplot() no seaborn e ajuda id padroes, correlações e outliers.
#Como cria grafico de dispersão com matplot e seaborn
#matplot: plt.scatter() colocando o x e y
#seaborn: sns.scatterplot() atribuindo os valores de x e y a variaveis anteriores

#O matplot é uma biblioteca básica e versatil para criar graficos em phyton com grande nível de controle
#O seaborn é uma biblioteca construída sobre o matplot e fornece uma interface de alto nivelpara criação de gráficos estatísticos mais atraentes e informativos
#O histograma é um tipo de gráfico que representa a distribuição de uma variável contínua dividindo-a em intervalos(lins) e contando o numero de informações em kd intervalo
#para criar um histograma vc usa plt.hist() fornecendo os dados e configurando os parametros
#As principais bibliotecas para visualização de dados são:Pandas, matplotlib, seaborn e cyborg

#quais dos gráficos é mais apropriado para avaliar a densidade de uma variável e identificar potenciais outliers? Densidade
#Os gráficos de densidade são uma bversão suavizada do histograma proporcionando uma visão continua da distribuição
#Sim, os graficos de densidade suavizam a distribuição o que pode ocultar picos acentuados que seriam vistos em um histograma
#sim, os graficos de regressão são usados para visualizar relações e não são indicados pra previsão de tendências futuras, embra possam sugerir padrões históricos
#Mapas de calor podem ser usados para visualizar a correlação de variáveis numéricas e categóricas (especialmente quando foi aplicada a codificação adequada)
#Gráficos de densidade são mais apropriados para variáveis contínuas
#mapas de calor são ideais para identificar correlções em um grande conjunto de dados
#graficos de dispersão são úteis para identificar padrões e outliers em variaveis quantitativas
#pairplot pode ficar confuso com mts variáveis causando confusão visual
#gráficos de contagem são mais úteis para visualização de frequencias em variaveis categoricas.











