import numpy as np

empregadoA = [70, 68, 71, 77, 65]
empregadoB = [62, 79, 72, 59, 85]

media_empregadoA = np.mean(empregadoA)
media_empregadoB = np.mean(empregadoB)

print(f'Empregado A teve uma média de: \n{media_empregadoA}\ne empregado B teve uma média de\n{media_empregadoB}')

"""
Calculado agora a amplitude de cada empregado
"""

amplitude_A = max(empregadoA) - min(empregadoA)
amplitude_B = max(empregadoB) - min(empregadoB)

"""
Qual empregado teve a maior amplitude?
"""
print('Amplitude empregado A: ',amplitude_A,'\nAmplitude empregado B: ',amplitude_B)

"""
Vamos calcular o desvio médio de cada um agora. Mas primeiro vamos entender o que é desvio médio.

Desvio é a diferença entre valores observados e a estimativa de localização
    ou seja, é a DIFERENÇA (SUBTRAÇÃO) entre a média e os valores dos elementos, exemplo:
        vamos supor que os dados são: notas = {6, 7, 3, 9}
        a média dessas notas é: 6 + 7 + 3 + 9 = 25 / 4 = 6,25
        o desvio médio é: 
            6 - 6.25 = -0.25
            7 - 6.25 = 1.25
            3 - 6.25 = -3.25
            9 - 6.25 = 2.75
            agora precisamos somar todos esses valores, e temos: 0.5 de desvio médio
                agora precisamos dividir esse 0.5 pelo tamanho dos dados, nesse caso 4:
                    0.5 / 4 = 0.125 de desvio médio
Desvio-padrão é a raiz quadrada da variância, sendo a que variância é a SOMA DOS QUADRADOS DOS DESVIOS DA MÉDIA
POR N - 1, EM QUE N É O NÚMERO DE VALORES DE DADOS
    sinonimo: erro médrio quadrático
Desvio absoluto médio é a raiz quadrada da variância
e isso é usado pra gente media a variabilidade

em um conjunto de dados x = {1, 4, 4} a média é 3 e a mediana é 4, cálculos:
 - sem numpy -
media = sum(x) / len(x)
media = 9 / 3
media = 3

mediana = valor que ocupa a posição CENTRAL dos dados, nesse caso o 4 (1, -4-, 4)

desvio medio
dm = (abs(soma(dados[k] - media) for k in dados)) / n
"""
mean_empregadoA = np.mean(empregadoA)
nA = len(empregadoA)

mean_empregadoB = np.mean(empregadoB)
nB = len(empregadoB)


dmA = [abs(empregadoA[k] - media_empregadoA) for k in range(0, nA)]
dmA = sum(dmA)
dma = dmA / nA
print(f'Desvio absoluto médio do empregado A é: {dmA}')

dmB = [abs(empregadoB[k] - media_empregadoB) for k in range(0, nB)]
dmB = sum(dmB)
dmB = dmB / nB
print(f'Desvio absoluto médio do empregado B é: {dmB}')

"""
Agora vamos calcular a variância desses dados:
"""
vA = [abs(empregadoA[k] - media_empregadoA)**2 for k in range(0, nA)]
vA = sum(vA)
vA = vA / nA
print('Variância do empregado A é: ', vA)

vB = [abs(empregadoB[k] - media_empregadoB)**2 for k in range(0, nB)]
vB = sum(vB)
vB = vB / nB
print('Variância do empregado B é:',vB)

dpA = np.sqrt(vA)
print('Desvio padrão de A: ',dpA)

dpB = np.sqrt(vB)
print('Desvio padrão de B: ', dpB)