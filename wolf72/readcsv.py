import csv
with open('../probieren.csv', newline='') as csvfile:
    csvData = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
    print(csvData.fieldnames)
    for row in csvData:
        print(row)