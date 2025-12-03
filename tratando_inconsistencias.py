
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


