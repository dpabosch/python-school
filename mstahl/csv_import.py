# coding: utf-8

seperator = ';'
csv = []

with open("../probieren.csv",encoding="utf-8") as file:
    columns = file.readline().strip().split(seperator)
    # print(columns)
    for line in file.readlines():
        values = line.strip().split(seperator)
        row = {}
        for i in range(len(values)):
            row[columns[i]] = values[i]
        csv.append(row)

for line in csv:
    print(line)
