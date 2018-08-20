import csv


def read_csv(filename, path='./', encoding='UTF-8', delimiter=';'):
    contentList = []
    try:
        with open(path+filename, encoding=encoding) as csvfile:
            csvData = csv.DictReader(csvfile, delimiter=delimiter)
            for row in csvData:
                contentList.append(row)
    except FileNotFoundError:
        print('Datei konnte nicht gefunden werden.')
    return contentList


def write_csv(filename, listOfEntrys, delimiter=';'):
    csvfile = open(filename, "w", encoding='utf-8', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=listOfEntrys[0].keys(), delimiter=delimiter)
    writer.writeheader()

    for row in listOfEntrys:
        writer.writerow(row)


if __name__ == '__main__':
    list_of_dicts_from_file = read_csv('probieren.csv', '../')
    write_csv('output_function.csv', list_of_dicts_from_file, delimiter=';')
