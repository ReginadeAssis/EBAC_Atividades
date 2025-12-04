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

