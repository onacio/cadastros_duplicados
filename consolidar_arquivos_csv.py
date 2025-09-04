'''
    Dados de entrada: arquivos csv do e-SUS APS - Cidadãos vinculados
    os arquivo csv devem ser armazenados na pasta 'dados' na raiz do projeto
    depois o script faz a junção dos dados em um unico arquivo 
'''

import pandas as pd
import os
import glob

# Caminho da pasta onde estão os arquivos CSV
pasta_csv = "dados"

# Encontra todos os arquivos .csv na pasta
arquivos = glob.glob(os.path.join(pasta_csv, "*.csv"))

# Lista para armazenar os DataFrames
lista_df = []

# Loop pelos arquivos
for arquivo in arquivos:
    try:
        # Lê o CSV a partir da linha 18 (skiprows=17)
        df = pd.read_csv(arquivo, encoding='latin1', sep=';', skiprows=17)
        lista_df.append(df)
        print(f"\u2705 Arquivo processado: {os.path.basename(arquivo)}")
    except Exception as e:
        print(f"\u274C Erro ao processar {arquivo}: {e}")

# Junta todos os DataFrames em um só
df_final = pd.concat(lista_df, ignore_index=True)

# Salva o resultado em um novo CSV
df_final.to_csv("dados_unificados.csv", sep=';', index=False)
print("\n \U0001F7E2 Todos os arquivos foram unificados com sucesso. \U0001F389")
