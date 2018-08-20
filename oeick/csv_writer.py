# coding: utf-8

import csv

reader = csv.DictReader(
           open('../probieren.csv', 'r', encoding='utf-8'),
           delimiter=';')

simple_dict = [{f: r[f] for f in r} for r in reader]
print(simple_dict)

field_names = list(simple_dict[0].keys())
print(field_names)

writer = csv.DictWriter(open('output.csv', 'w', newline='', encoding='utf-8'), field_names, delimiter=';')
writer.writeheader()
for r in simple_dict:
    writer.writerow(r)
