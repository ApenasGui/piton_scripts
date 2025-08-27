num_lotes = [14, 46, 58, 76, 68, 62, 48, 22, 6]
sum_lotes = sum(num_lotes)
at = 1200 - 300
print(at)
freq_acum = 0
i = 0

for i in range(2, 6):
    freq_acum += num_lotes[i]

print(freq_acum)

relat = freq_acum / sum_lotes
relat = relat * 100
print(relat)