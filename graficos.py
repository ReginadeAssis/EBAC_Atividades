import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes_v3_preparado.csv')
print(df.head().to_string())

# Teste com histograma
plt.hist(df['salario'])
plt.show()
 #O histograma é usado para mostrar a distribuição dos dados ai dentro do .hist( coluna desejada), coloca o .show pq
 #dependendo da biblioteca ele não vai exibir

 #Teste de histogramas com parâmetros
plt.figure(figsize =(10,6)) #Define o tamanho da figura
plt.hist(df['salario'], bins=100, color='blue', alpha=0.5)
#.hist(coluna, inicio do grafico, cor, transparencia)
plt.title('Histograma-Salários')
plt.xlabel('Salário') #legenda do eixo x e dps do y
plt.ylabel('Quantidade')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000,2000))
#O ticks define o intervalo (inicio, fim que é o maior salario, intervalo)
plt.grid(True)
plt.show()

#Unindo multiplos gráficos
plt.figure(figsize =(10,6))
plt.subplot(2,2,1)
#o subplot é onde vai ficar posicionado o gráfico (linha 2, coluna 2 e grtafico 1)
#Gráfico de dispersão:
plt.scatter(df['salario'], df['salario'])#Colocou assim pq a variável sal´rio é a que vai no x e no y
plt.title('Dispersão do Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')
  #se vc observar faz reta perfeita correlação de 100% pq os pontos se cruzam

#Grafico 2 tbm de dispersão:
plt.subplot(1,2,2) #aqui é como q vai posicionar o grafico(linha, coluna e grafico)
plt.scatter(df['salario'],df['anos_experiencia'], color ='#588398', alpha = 0.6,s=30) #.scatter(define x, define y, cor, transparencia e tamanho

#Mapas de calor
corr= df[['salario','anos_experiencia']].corr() #primeiro vc cria uma variável c os itens q vc quer correlacionar
plt.subplot(2,2,3) #(linha, coluna, n do gráfico)
sns.heatmap(corr, annot = True, cmap='viridis')
plt.title('Relação Salário e Idade')
plt.tight_layout() #ajusta o espaçamento é ipc p gráficos p evitar sobreposição
plt.show()

#Uso de Matplot é uma biblioteca que cria diversos gráficos
#Gráfico de barra

plt.figure(figsize =(10,6)) #determina o tamanho daquela figura grande
df['nivel_educacao'].value_counts().plot(kind='bar', color ="#90ee70") #df[coluna de dado que vai usar].value(pq tem opção de índice e valor e aqui é valor)
# .plot é função do pandas kind é o tipo de gráfico no caso kind o de barra e a cor #...
plt.title('Divisão escolaridade -1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0) #Qual grau vai ficar o eixo x q vai dar a inclinação pode ser yticks tbm
plt.show()


#Também dá para fazer o gráfico de barras atribuindo um valor a y e y primeiro

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values
plt.figure(figsize =(10,6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade -2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.show()

#Gráfico de Pizza
plt.pie(y, labels=x, autopct='%1.0f%%', startangle=90) #usa o mesmo x e y de cima autopct é como ele vai mostrar aqui no caso em %
# e o startangle é o angulo que começa aqui ele coloca 90°
plt.title('Distribuição de Nivel')
plt.show()

#Gráfico de Dispersão/correlação
plt.hexbin(df['idade'], df['salario'],gridsize=40,cmap='Blues') #define x, y, tamanho da bolinha, cor do mapa
plt.colorbar(label='Contagem dentro do bin') #é a escala lateral de cor que mostra a concentração
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

#Uso de seaborn é feito pq tem mais recursos de agrupamento e estatística, mas é também uma biblioteca baseada no matplot
#Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') #(x, y, de onde vem e tipo de visualização pode ser hist, hex...
plt.show()

#Gráfico de Densidade mostra a distribuição dos dados e suaviza o histograma montando uma curva de distribuição
sns.kdeplot(df['salario'], fill =True, color ='#863E9C') #Esse kdplot é ele chamando o grafico
plt.title('Densidade de Salários')
plt.xlabel('Salario')
plt.show()

#Gráfico de pairplot, dispersão e histograma pq esse pairplot é capaz de criar relacionando mais de um campo
sns.pairplot(df[['idade','salario', 'anos_experiencia','nivel_educacao']])
plt.show()

#O gráfico de regressão vai calcular a linha que une os dois campos
sns.regplot(x='idade', y='salario', data=df, color='#278f65',scatter_kws = {'alpha': 0.5, 'color':'#34c289'})
#o primeiro color é a cor a linha da dispersão o segundo o scatter é a cor da dispersão
plt.title('Regressão de salário por idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

#Gráfico countplot com hue(mostra os agrupamentos)
sns.countplot(x='estado-civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estad Civil')
plt.ylabel('Quantidade')
plt.legend(title='Nível de Educação') #isso é o título da legenda das diferentes cores
plt.show()






















