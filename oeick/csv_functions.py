# encoding: utf-8

import csv

ENCODING = 'utf-8'


def read_csv_file(filename, delimiter=';'):
    reader = csv.DictReader(open(filename, 'r', encoding=ENCODING),
                            delimiter=delimiter)
    return [{f: r[f] for f in r} for r in reader]


def write_csv_file(filename, list_of_dicts, delimiter=';'):
    field_names = list_of_dicts[0].keys()
    writer = csv.DictWriter(open(filename, 'w', newline='', encoding=ENCODING),
                            field_names,
                            delimiter=delimiter)
    writer.writeheader()
    for r in list_of_dicts:
        writer.writerow(r)


def print_list_of_dict(list_of_dicts):
    for row in list_of_dicts:
        print(row)


if __name__ == '__main__':
    list_of_dicts_from_file = read_csv_file('../probieren.csv')
    print_list_of_dict(list_of_dicts_from_file)
    write_csv_file('output_function.csv', list_of_dicts_from_file, delimiter=',')
