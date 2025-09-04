import pandas as pd

idades = [
    23, 19, 20, 33, 25, 23, 24, 21, 29, 17
]

indicies = [
    'Roberto', 'Amanda', 'Júlia', 'Pedro', 'Spike', 'Tempestade', 'Ciclope', 'Ramsay', 'Ellie', 'Joel'
]

idades_series = pd.Series(idades, index=indicies)
print(idades_series)

# qual é a pessoa mais velha? Escreva o nome e a idade
print(f'A pessoa mais velha da sala é: {idades_series.idxmax()} com {max(idades)} anos')

# qual a média de idade da sala?
print('A média da sala é: ',idades_series.mean())

#qual é a mediana da sala?
summary_idades = idades_series.describe()
print(summary_idades.iloc[5]) # acessa a serie de 50% na serie dos sumários

# e qual é a variância dessa sala?
var_idades = idades_series.var() # variance
print(var_idades)

# e o desvio padrão dessa turma?
desvio_idades = idades_series.std() # standard deviation
print(desvio_idades)

# quais são as 3 pessoas mais velhas e mais novas da sala?
ordem_idades = idades_series.sort_values()
menores_idades = ordem_idades.iloc[:3]
print(f'Os mais jovens são:\n{menores_idades}')

maiores_idades = ordem_idades.iloc[-3:]
print(f'Os 3 alunos mais velhos são:\n{maiores_idades}')