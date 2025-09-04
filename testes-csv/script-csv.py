import csv
idades = []

with open('exemplo.csv', mode='r', encoding='utf-8') as arq:
    text = csv.DictReader(arq)
    for line in text:
        pessoaMaiorIdade = max(text, key=lambda line: int(line['idade']))
        pessoaMenorIdade = min(text, key=lambda line: int(line['idade']))
        idade_str = line['idade']
        idade_int = int(idade_str)
        idades.append(idade_int)

media_idade = sum(idades) / len(idades)
print(f'A média de idades da rapaziada é: {media_idade}')

print(f'A pessoa mais velha da lista tem: {max(idades)} que é o {pessoaMaiorIdade['nome']}')
print(f'A pessoa com menor idade tem {min(idades)} e seu nome é {pessoaMenorIdade['nome']}')