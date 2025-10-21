'''
Este script recebe um arquivo csv consolidado que foi gerado no arquivo [consolidar_arquivos_csv.py]
ou um relatório de Cidadãos vinculados do e-SUS APS diretamente
e faz a extração de registros duplicados com base nas colunas Nome e Data de nascimento.
'''
import pandas as pd


# Use essa linha para utilizar o .csv gerado do script [consolidar_arquivos_csv.py]
#df = pd.read_csv('dados_unificados.csv', sep=';', encoding='utf8')

# Use essa linha para utilizar o relatório do e_SUS APA diretamente [Cadastros vinculados]
df = pd.read_csv('dados\\sede1.csv', sep=';', encoding='latin1', skiprows=17)

# Considera como duplicadas as linhas com mesmo nome e data de nascimento
duplicados = df[df.duplicated(subset=["Nome", "Data de nascimento"], keep=False)]

# Salvar em um novo arquivo
#duplicados.to_csv("cadastros_duplicados.csv", sep=';', encoding='latin1', index=False)
duplicados.to_excel("cadastros_duplicados.xlsx", index=False)