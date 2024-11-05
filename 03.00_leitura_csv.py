import pandas as pd

# Exemplo de carregamento de arquivo csv [Comma Separeted Values]
df = pd.read_csv('data.csv') # read_csv('') -> carrega o arquivo no DataFrame
print('-----Exemplo do uso do to_string(impressão TOTAL)-----')
#print(df.to_string())        # to_string() -> imprime o DataFrame INTEIRO

# Print sem o parâmetro acima, ele só imprime as 5 primeiras e as 5 últimas linhas
print('-----Exemplo de print direto-----')
#print(df)

# max_rows = essa opção mostra a configuração do sistema para a impressão de linhas, o padrão 60, caso o arquivo tenha mais desse limite, ele só imprimirá as 5 primeira e últimas linhas. Você pode determinar no código esse número máximo:
pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)

