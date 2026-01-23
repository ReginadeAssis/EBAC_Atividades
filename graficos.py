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





