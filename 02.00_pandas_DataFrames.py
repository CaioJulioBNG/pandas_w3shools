import pandas as pd

# DataFrames é uma estrutura de duas dimensoẽs, uma tabela com linhas e colunas
data = {
  "calorias": [420, 380, 390],
  "duração": [50, 40, 45]
}
df = pd.DataFrame(data) #carregando os dados no DataFrame
print('-----Exemplo de DataFrame-----')
print(df)

# Localizar a linha
print('-----Print de uma única linha(row)-----')
print(df.loc[[0,1]]) ## imprimir 2 linhas, para uma única, tire 1 []

# Index Personalizados: Praticamente igual a series
df_perso = pd.DataFrame(data, index = ['dia 1', 'dia 2', 'dia 3'])
print('-----DataFrame com Index Personalizado-----')
print(df_perso)
