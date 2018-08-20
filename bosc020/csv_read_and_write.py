import csv;


def import_csv(filename):
    csvReader = csv.DictReader(open(filename, newline='', encoding='utf-8'), delimiter=';', quotechar='|')
    list_of_entrys = []
    for row in csvReader:
        list_of_entrys.append(row)
    return list_of_entrys


def write_csv(filename, fieldnames, listOfEntrys):
    csvfile = open(filename, "w", encoding='utf-8', newline='')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()

    for row in list_of_entrys:
        writer.writerow(row)


list_of_entrys = import_csv('../probieren.csv')
write_csv("output.csv", list_of_entrys[0].keys(), list_of_entrys)
