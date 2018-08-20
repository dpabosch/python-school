import csv
with open('../probieren.csv', newline='') as csvfile:
    csvData = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
    print(csvData.fieldnames)
    for row in csvData:
        print(row)

def readCSV(filename, path='./', encoding='UTF-8', delimiter=''):
    contentList = []
    try:
        with open(path+filename, encoding=encoding) as csvfile:
            csvData = csv.DictReader(csvfile, delimiter)
        for row in csvData:
            contentList.append(row)
    except FileNotFoundError:
        print('Datei konnte nicht gefunden werden.')
    return contentList


contentList = readCSV('probieren.csv')