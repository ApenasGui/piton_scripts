import pandas as pd

dados = pd.DataFrame({
    "Sexo": ["M", "M", "F", "M", "F"],
    "Idade": [24, 32, 22, 18, 29]
})
print(dados.dtypes)