# coding: utf-8

seperator_in = ';'
csv = []

# Beispieldatei auslesen
with open("../probieren.csv",encoding="utf-8") as file:
    columns = file.readline().strip().split(seperator_in)
    # print(columns)
    for line in file.readlines():
        values = line.strip().split(seperator_in)
        row = {}
        for i in range(len(values)):
            row[columns[i]] = values[i]
        csv.append(row)

# Daten schreiben
# Schreibe vor jede Zeile eine id (aufsteigend) und verwende als serpator ein Komma
seperator_out = ","
with open("probien_mit_id.csv",'w',encoding="utf-8") as file:
    # schreibe header
    header = "id" + seperator_out + seperator_out.join(csv[0].keys())
    file.write(header+"\n")
    # schreibe daten zeilenweise
    for line in csv:
        id = str(csv.index(line)+1)
        out_line = seperator_out.join(line.values())
        row= id + seperator_out + out_line + "\n"
        file.writelines(row)

with open("probien_mit_id.csv",encoding="utf-8") as file:
    for line in file.readlines():
        print(line.strip())