import csv;


def import_csv(filename):
    csvReader = csv.DictReader(open(filename, newline='', encoding='utf-8'), delimiter=';', quotechar='|')
    list_of_entrys = []
    for row in csvReader:
        list_of_entrys.append(row)
    return list_of_entrys


def write_csv(filename, listOfEntrys):
    csvfile = open(filename, "w", encoding='utf-8', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=listOfEntrys[0].keys(), delimiter=',')
    writer.writeheader()

    for row in listOfEntrys:
        writer.writerow(row)


list_of_entrys = import_csv('../probieren.csv')
write_csv("output.csv", list_of_entrys)
