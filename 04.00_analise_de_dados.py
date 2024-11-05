import pandas as pd

# Método para exibir um determinado número de linhas [TOPO]
df = pd.read_csv('sentiment140.csv', delimiter=';')
print('-----Print das 10 primeiras linhas-----')
##print(df.head(10)) # Por padrão, caso não seja definido, exibirá as 5 primeiras linhas

# Método para exibir um determinado número de linhas [FINAL]
print('-----Print das 10 últimas linhas-----')
##print(df.tail()) # Por padrão, caso não seja definido, exibirá as 5 primeiras linhas

# Método para receber informações sobre o data set
print('-----Exibindo informações sobre o data set')
print(df.info())