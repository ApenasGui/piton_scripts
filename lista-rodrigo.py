from collections import Counter
from math import log10
from decimal import ROUND_HALF_UP, Decimal

"""notas de 120 alunos, 4 turmas, do terceiro ano de uma escola"""

dados = [60, 61, 62, 63, 63, 64, 65, 66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70,
70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 73, 73, 73, 73, 74, 74, 74, 74, 74,
75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78,
79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 83,
83, 83, 83, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 87, 87, 87, 87, 87, 87, 90, 92, 97]

totalAlunos = 120

frequencia = Counter(dados)

print(frequencia)

"""calculando média sem libs"""
media = sum(dados) / totalAlunos
print(f'A média de totas as notas é igual a: {media:.2f}')

"""calculanto amplitude total"""
at_notas = max(dados) - min(dados)
print('A amplitude total de notas é: ',at_notas) 

"""agora vamos calcular o desvio médio dessas notas"""
dm_notas = [abs(dados[k] - media) for k in range(0, totalAlunos)]
dm_notas = sum(dm_notas) / totalAlunos
print(f'Desvio padrão das notas de 120 alunos é: {dm_notas:.4f}')

"""agora, vamos contruir uma tabela a partir dos dados"""
"""primeiro, precisamos saber quantas classes essa tabela terá"""

k = 1 + (3.3 * log10(totalAlunos))
print(f'A tabela terá {round(k)} classes')

"""calculando o intervalo das classes"""
h = at_notas / k
print(f"O intervalo de cada classe será de: {round(h)}")

