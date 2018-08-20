# coding: utf-8

import csv

reader = csv.DictReader(
         open('../probieren.csv', 'r', encoding='utf-8'),
         delimiter=';')

for row in reader:
    print("Zeile {}: {}".format(reader.line_num, row))
    for field in row:
        print("    {:12}: {}".format(field, row[field]))
