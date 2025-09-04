import pandas as pd

idades = [
    34, 35, 29, 26, 26, 22, 32, 35, 27, 30, 23, 23, 26, 35, 30, 32, 22, 33, 34, 32,
20, 26, 29, 21, 27, 23, 24, 32, 31, 24, 22, 33, 32, 35, 30, 24, 25, 20, 26, 35,
21, 23, 24, 32, 31, 24, 22, 33, 32, 35
]

# calculos sem python
soma_idades = sum(idades)
num_idades = len(idades)
media_idade = soma_idades / num_idades
print('Media de idades é: ', media_idade)

# calculando a variancia
diff = 0
for i in idades:
    diff += (i - media_idade)**2

variancia = diff / num_idades
print('Variância: ', variancia)

# desvio padrão
dpm_idade = [abs(idades[k] - media_idade) for k in range(0, num_idades)]
dpm_idade = sum(dpm_idade) / num_idades
print('Desvio padrão média é: ', dpm_idade)

# agora calculando com series do pandas

idades_series = pd.Series(idades)
print(idades_series)

print(
idades_series.mean(),
idades_series.var(),
idades_series.describe()
)
