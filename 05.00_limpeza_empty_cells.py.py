import pandas as pd

# Remoção da linha com uma Célula vazia
df = pd.read_csv('e_data.csv')
new_df = df.dropna()              # dropna() cria um novo dataframe, sem mosdificar o original
#df.dropna(inplace = True)        # inplace - True, incica para modificar o dataframe original
#print(new_df.to_string())        # relembrando, to_string() imprime o dataset inteiro

# Substituição de valores nulos   
# df.fillna(130, inplace = True)               # Substitui o valor nulo com o parâmetro '130'
# df['Calories'].fillna(130,inplace - True)    # Substitui apenas na coluna de Calorias

# Substituição com MEAN(Média), Median(Mediana), Mode(Moda)

x = df['Calories'].mean()      # Média
x = df['Calories'].median()    # Mediana
x = df['Calories'].mode()      # Moda

df['Calories'].fillna(x, inplace=True) # Padrão 