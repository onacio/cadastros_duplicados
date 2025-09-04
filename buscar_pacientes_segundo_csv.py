import pandas as pd

df1 = pd.read_csv('sede_1_cad_invalidos.csv', sep=';', encoding='latin1', skiprows=11)
df2 = pd.read_csv('dados_unificados.csv', sep=';', encoding='utf8')

resultado = pd.merge(df1, df2[['Nome equipe', 'Microárea']], on='Nome', how='left')

resultado.to_excel('resultado_teste.xlsx', index=False)