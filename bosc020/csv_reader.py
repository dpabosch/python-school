import csv;

spamReader = csv.DictReader(open('probieren.csv', newline='', encoding='utf-8'), delimiter=';', quotechar='|')

list_of_entrys = []
for row in spamReader:
    list_of_entrys.append(row)