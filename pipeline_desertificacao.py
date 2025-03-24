import pandas as pd

# Definir o caminho do arquivo
caminho_arquivo = 'data/desertificacao_solos.xlsx'

# Carregar os dados do Excel
df = pd.read_excel(caminho_arquivo, engine='openpyxl')

# Exibir as primeiras linhas do DataFrame
print("Visualização inicial dos dados:")
print(df.head())

# Exemplo de limpeza: remover linhas com valores nulos
df_limpo = df.dropna()

# Exemplo de transformação: renomear colunas para minúsculas
df_transformado = df_limpo.rename(columns=str.lower)

# Salvar o DataFrame transformado em um novo arquivo Excel
caminho_saida = 'data/desertificacao_solos_tratado.xlsx'
df_transformado.to_excel(caminho_saida, index=False, engine='openpyxl')

print(f"Pipeline concluído. Dados tratados salvos em '{caminho_saida}'.")