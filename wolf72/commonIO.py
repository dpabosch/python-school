import csv
import os.path

def readCSV(filename, path='./', encoding='UTF-8', delimiter=';'):
    contentList = []
    try:
        with open(os.path.join(path, filename), encoding=encoding) as csvfile:
            csvData = csv.DictReader(csvfile, delimiter)
            for row in csvData:
                contentList.append(row)
    except FileNotFoundError:
        print('Datei konnte nicht gefunden werden.')
    return contentList


contentList = readCSV('probieren.csv', '../')
print(contentList)

