import pandas as pd

# 'serie' em panda é uma coluna de uma tabela
a = [0, 5, 7]
var = pd.Series(a)
print('-----Exemplo de Series-----')
print(var)

# Se não for colocado manualmente, os valores terão uma 'label' de acordo com o seu index, começando com o 0,
print('-----Exemplo de um Print filtrando pela label-----')
print(var[0])

# É possível criar labels
var1 = pd.Series(a, index = ['a','b','c'])
print('-----Exemplo de Labbels Modificadas-----')
print(var1)

# Pode se usar pares de chave-valor (dicionário) para criar uma serie
estoque = {'janeiro': 1000, 'fevereiro': 900, 'marco': 550}
var2 = pd.Series(estoque)
print('-----Exemplo de serie com um dicionário-----')
print(var2)

# Pode se filtrar os itens a serem imprimidos
var3 = pd.Series(estoque, index = ['janeiro', 'fevereiro'])
print('-----Exemplo de filtragem por index-----')
print(var3)

# DataFrames: enquanto series são uma coluna, DataFrames são a tabela inteira
dados = {
    "Meses": ['janeiro', 'fevereiro', 'marco'],
    "Estoque": [500, 300, 150],
    "Vendas": [0, 200, 150]
}
var4 = pd.DataFrame(dados)
print('-----Exemplo de DataFrame-----')
print(var4)