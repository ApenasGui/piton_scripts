Fzao = [2, 9, 21, 29, 34]
fzinho = []
k= 0

for k in range(1, len(Fzao)):
    elemento = Fzao[k] - Fzao[k-1]
    fzinho.append(elemento)

print(fzinho)

"""
Respondendo exercícios do livro 'Estatística Fácil' em python
"""

lista = [14, 12, 11, 13, 14, 13,
12, 14, 13, 14, 11, 12,
12, 10, 14, 13, 15, 11,
15, 13, 16, 17, 14, 14]

i = 0
d=0
o=0
do=0
t=0
q=0
qu=0
deze=0
sete=0

for i in range(len(lista)):

    if lista[i] == 10:
        d = d + 1
    if lista[i] == 11:
        o = o + 1
    if lista[i] == 12:
        do = do + 1
    if lista[i] == 13:
        t = t + 1
    if lista[i] == 14:
        q = q + 1
    if lista[i] == 15:
        qu = qu + 1
    if lista[i] == 16:
        deze = deze + 1
    if lista[i] == 17:
        sete = sete + 1

print(d, o, do, t, q, qu, deze, sete)

"""
isso tudo pode ser resolvido apenas com o Counter, um contador que já faz a contagem automaticamente
"""

from collections import Counter

freq = Counter(lista)

print(freq)