import pandas as pd

idades = [
    34, 35, 29, 26, 26, 22, 32, 35, 27, 30, 23, 23, 26, 35, 30, 32, 22, 33, 34, 32,
20, 26, 29, 21, 27, 23, 24, 32, 31, 24, 22, 33, 32, 35, 30, 24, 25, 20, 26, 35,
21, 23, 24, 32, 31, 24, 22, 33, 32, 35
]

series_idades = pd.Series(idades)

series_idades = series_idades.sort_values()


# os índices da séries, funcionam da mesma maneira que os índicies do dicionário
# o índice também fica VINCULADO ao número da série, ou seja, um elemento da série de valor 30 na posição 5
# se reordenarmos o 5 SEMPRE vai ser do elemento 30
series_idades.iloc[:5]