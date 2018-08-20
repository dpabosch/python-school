def csv_import(dateipfad,seperator=";"):
    csv = []
    # Beispieldatei auslesen
    with open(dateipfad, encoding="utf-8") as file:
        columns = file.readline().strip().split(seperator)
        # print(columns)
        for line in file.readlines():
            values = line.strip().split(seperator)
            row = {}
            for i in range(len(values)):
                row[columns[i]] = values[i]
            csv.append(row)
    return csv

def csv_export(dateipfad,list_of_dicts,seperator=";"):
    with open(dateipfad, 'w', encoding="utf-8") as file:
        # schreibe header
        header = "id" + seperator + seperator.join(list_of_dicts[0].keys())
        file.write(header + "\n")
        # schreibe daten zeilenweise
        for line in list_of_dicts:
            id = str(list_of_dicts.index(line) + 1)
            out_line = seperator.join(line.values())
            row = id + seperator + out_line + "\n"
            file.writelines(row)

def print_file(dateipfad):
    with open(dateipfad, encoding="utf-8") as file:
        for line in file.readlines():
            print(line.strip())