import pandas as pd

# Carregue o DataFrame a partir do arquivo CSV
df = pd.read_csv("data/Mall_Customers.csv")

# Remova a coluna 'CustomerID' se ela existir
if 'CustomerID' in df.columns:
    df.drop('CustomerID', axis=1, inplace=True)

# Use a função 'map' para codificar 'Male' como 0 e 'Female' como 1 na coluna 'Gender'
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Se você tiver outras colunas no DataFrame que precisam ser mantidas, não se esqueça de incluí-las

# Se quiser verificar o resultado, imprima o DataFrame
print(df)

# Salve o DataFrame resultante em um arquivo CSV
df.to_csv('dados_codificados.csv', index=False)
