import csv

with open('exemplo.csv', encoding='utf-8') as archive:
    text = csv.reader(archive)
    for line in text:
        print(line)