import numpy as np

num_lotes = [14, 46, 58, 76, 68, 62, 48, 22, 6]
metragem_lotes = [300, 400, 500, 600, 700, 800, 900, 1000, 1100]
for i in range(0, len(num_lotes)):
    print(num_lotes[i], metragem_lotes[i])

media_lotes = np.mean(num_lotes)
print('Média dos moradores por lote é: ',media_lotes)

at_lotes = max(num_lotes) - min(num_lotes)
print('Amplitude dos lotes é: ',at_lotes)

n_lotes = len(num_lotes)

dm_lotes = [abs(num_lotes[k] - media_lotes) for k in range(0, n_lotes)]
dm_lotes = sum(dm_lotes) / n_lotes
print('Desvio padrão dos moradores dos lotes é: ',dm_lotes)