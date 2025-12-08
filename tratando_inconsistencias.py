import numpy as np
import pandas as pd

df = pd.read_csv('clientes_remove_outliers.csv')

#primeiro ele chama a planilha q ele quer ler e já executa p ficar td redondo com shift f10
print(df.head())

# Lembre tbm q algumas vezes não é sobre excluir é sobre ocultar então se pode criar o q ele chamou de máscara

df['cpf_mascara'] = df['cpf'].apply(lambda cpf: F'{cpf[:3]}.***.***-{cpf[-2:]}')
#Criou o campo cpf mascara e ele recebe campo cpf com alterações promovidas pela função lambda
#o campo cpf será formatado para mostrar apenas os 3 primeiros e os 2 últimos

#Também é importante das atenção ao formato das datas
df['data'] = pd.to_datetime(df['data'], format ='%y%m%d' , errors = 'coerce')

#Alterou também para pessoa não ter nascido hj ou no futuro
data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data']<= data_atual, pd.to_datetime('1900-01-01'))
#Assim ele faz um filtro q caso a data seja menor q a atal ele põe 1900 no lugar p tanto cria uma variável q recebe a data de hj


df['idade_ajustada'] = data_atual.year -df['data_atualizada'].dt.year
#Cria o campo idade ajustada q é a data atual - data atulizada q é a q em a ajuste q remove bbs do futuro

df['idade_ajustada'] = ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
#Cuidado, pq ainda é preciso manter a idade atualizada se hj vc tem 20 ano q em tem 21 e o banco de dados fica c dados atrasados
#P evitar que dê erro cntando com o mês ele precisa de mais código e remove um se a data atual for menor q a atualizada
#O bloco retornaria v ou f ai coloca como int p sair 0 ou 1

#Já para para os valores acima de 100 optou por usar a biblioteca numpy q vai colocar no campo o valor nulo
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] =np.nan

#Criou o campo endereço correto e onde tem o \n ele vai separar pulando linha
df['endereco_certo'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
#Coloca o [0] p dizer p ele pegar o primeiro o .strip é p garantir q n vai ter espaço. No campo endereço ele pega
#e dentro dele n pega só o conteúdo x diz faz blocos c o espaço começando do primeiro e dps remove

#Aqui ele cria o campo bairro que recebe o segundo elemento se tiver caso menor q um bloco recebe endereço desconhecido
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n'))> 1 else 'Desconhecido')

#A ideia para o estado foi semelhante
df['estado_sigla']= df['endereco'].apply(lambda x: x.split('/')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')

#Agr ele foi p o conteúdo do campo. Entre 50 e 5 letras endereço inválido do contrário pega o endereço da coluna endereço
df['endereco_curto'] = df['endereco'].apply (lambda x :'Endereço Inválido' if len(x) > 50 or len(x) < 5 else x )
print('Qtd', (df['endereco_curto'] == 'Endereço Inválido').sum())

#Agr ele quer tornar o campo cpf inválido de acordo c o tamanho do conteúdo. se o tamnho for 14 se mantém e copia o x
#Caso contrário coloca inválido
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'cpf inválido') #x if tamanho de x for 14 do contrário cpf inválido
print('Qtd', (df['cpf'] == 'cpf inválido').sum()) #P ver é o campo q eu quero c o valor q quero .sum p ele somar

#p conferir os estados ele pegou a lista de estados brasileiros no google
estados_br = ['AC','AP','AM','PA','RO','RR','TO','AL','BA','CE','MA','PB','PE','PI','RN','SE','DF','GO','MT','MS','ES','MG','RJ','SP','PR','RS','SC']
df['estado_sigla']= df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'desconhecido')
#dps da arrumação vc joga isso p campo q já tinha nome
print('Qtd', (df['estado_sigla'] == 'desconhecido').sum())

#Dps de arrumar vc joga isso p os campos q já tinham nome
df['cpf'] = df['cpf_mascara']
df['idade']= df['idade_ajustada']
df['endereco']= df['endereco_curto']
df['estado']= df['estado_sigla']

#Dps ele atualiza e salva os campos manualmente p garantir e salvar em um novo arquivo:
df_salvar = df[['nome','cpf','idade','data','endereco','estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)
#p fechar pede p exibir
print('novo data frame:\n', pd.read_csv('clientes_tratados.csv'))

#Alguns conceitos importantes:
#Zscore é uma medida estatística que indica quantos dp um valor está distante da média de um conjunto de dados
# é comum seu uso para identificar outliers
#Lambda é uma expressão anônima em phyton que permite a criação de pequenas funções descartáveis sendo ´til para operações simples e rápidas
#IQR-interquartile range é uma medida estatística que representa a diferença entre o 1,3 quartil e o conjunto de dados, tbm usada p id aoutlier
#Fillna- é uma função da biblioteca pandas que permite substituir valores nulos em um dataframe por um valor específico ajudando a lidar c dados ausentes
#Dropna é uma função da biblioteca pandas usada p remover valores nulos d e u data frame. Pode ser usada p eliminar linhas e colunas inteiras q contém valores nulos
#Dataframe é uma estrutura de dados bidimensional semelhante a uma tabela que é usada para armazenar e manipular dados em phyton
#especialmente com a biblioteca pandas cada coluna de um dataframe pode conter diferentes tipos de dados

#Para exploração inicial dos dados é essencial entender a estrutura dos dados por isso se usa funções como
#head e tail para visualizar os primeiros e últimos registros identificando os padrões e inconnsistências

#Verificação dos dados: verifique a quantidade de linhas e colunas tipos de dados e valores nulos do dataframe, isso ajuda a id problemas em potencial q precisam de correção
#A biblioteca panas é uma ferramenta importante com phyton importar dados de arquivos csv para um dataframe panda facilita a analise e o tratamento de dados











