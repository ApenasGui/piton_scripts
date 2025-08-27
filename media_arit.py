"""
média aritmédica
soma dos dados / número de elementos
"""
x = [25, 40, 50]

media = sum(x)/ len(x)
print("Média utilizando a fórmula completa",media)

"""
Ou dá pra fazer com uma biblioteca, o que já faz tudo pra gente de forma automática
"""
import numpy as np
print('Média com Numpy',np.mean(x))
