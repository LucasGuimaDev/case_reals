import pandas as pd

df_colaborador_agencia = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\colaborador_agencia.csv')
df_agencias = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\agencias.csv', encoding='latin1')
df_clientes = pd.read_excel(r'C:\Users\sonia\Desktop\case_reals\arquivos\clientes.xlsx')
df_colaboradores = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\colaboradores.csv', encoding='latin1')
df_contas = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\contas.csv')
df_propostas = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\propostas_credito.csv', encoding='latin1')
df_transacoes = pd.read_csv(r'C:\Users\sonia\Desktop\case_reals\arquivos\transacoes.csv', encoding='latin1')

print(df_clientes.info())
print(df_colaborador_agencia.info())
print(df_agencias.info())
print(df_colaboradores.info())
print(df_colaboradores.info())
print(df_contas.info())
print(df_propostas.info())
print(df_transacoes.info())
