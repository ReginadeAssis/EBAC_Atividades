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
