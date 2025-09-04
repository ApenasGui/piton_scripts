import csv

with open('exemplo.csv', encoding='utf-8') as archive:
    txt = csv.DictReader(archive)
    for lane in txt:
        menorIdade = min(txt, key=lambda line: )
        maiorIdade = max(txt, key=lambda line: )

print(menorIdade)
print(maiorIdade)