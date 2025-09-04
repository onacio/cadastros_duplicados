'''
Este script recebe um arquivo csv consolidado do relatório de Cidadãos vinculados do e-SUS APS
e faz a extração de registros duplicados com base nas colunas Nome e Data de nascimento.
'''
import pandas as pd

# Carregar base de dados
#df = pd.read_csv('dados_unificados.csv', sep=';', encoding='utf8')
df = pd.read_csv('dados/sede1.csv', sep=';', encoding='latin1', skiprows=17)

# Considera como duplicadas as linhas com mesmo nome e data de nascimento
duplicados = df[df.duplicated(subset=["Nome", "Data de nascimento"], keep=False)]

# Salvar em um novo arquivo
duplicados.to_csv("dados_duplicados.csv", sep=';', index=False)