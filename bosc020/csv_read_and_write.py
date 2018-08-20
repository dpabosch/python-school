import csv;

csvReader = csv.DictReader(open('../probieren.csv', newline='', encoding='utf-8'), delimiter=';', quotechar='|')

list_of_entrys = []


csvfile=open("output.csv", "w", encoding='utf-8', newline='')
writer = csv.DictWriter(csvfile, fieldnames=csvReader.fieldnames, delimiter=',')
writer.writeheader()

for row in csvReader:
    print(row)
    list_of_entrys.append(row)

for row in list_of_entrys:
    writer.writerow(row)



