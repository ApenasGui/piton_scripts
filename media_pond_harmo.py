#dados
x = [10,60,360]
y = [2,2,2,2]

"""
média harmônica (xh)
xh = (1/(soma(1/xj)))
xh = n / (sum(1/xj))

pág. 134 cáp 4

cálculo manual:
"""
nX = len(x)
somaX = (1 / x[0] + (1 / x[1]) + (1 / x[2]))
print(f'Média harmônica = {nX} / {somaX: .4f}')

"""
Agora vamos fazer importando as bibliotecas em numPy
"""
import numpy as np
import statistics as sts

c = [0.5, 0.7]
print(sts.harmonic_mean(x))

xh = nX / somaX
print(f'Média hamônica = {xh:.4f}')