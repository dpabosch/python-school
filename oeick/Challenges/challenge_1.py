# encoding=utf-8

import oeick.csv_functions as csvf
import sqlite3
import doctest

PERSON = 1
ADRESSE = 2
BEIDE = 3


class ChallengerOne:

    def __init__(self):
        self.db = None
        self.column_names = None

    def read_data(self, file_name):
        list_of_dicts = csvf.read_csv_file(
            file_name,
            delimiter=';',
            encoding='latin-1')
        return list_of_dicts

    def create_database(self, list_of_dicts):
        self.column_names = self.get_column_names_from_dict(list_of_dicts[0])
        self.db = sqlite3.connect(r'C:\Users\eick036\repos\python-school\oeick\Challenges\challenge.db')
        cursor = self.db.cursor()
        sql = "create table if not exists PERSON ( " + \
              "NR integer primary key, " + ', '.join(["{} text".format(f) for f in self.column_names[1:]]) + \
              ");"
        cursor.execute(sql)

    @staticmethod
    def get_column_names_from_dict(dict_with_table_rows):
        """
        >>> ChallengerOne.get_column_names_from_dict(dict_with_table_rows={})
        []
        >>> ChallengerOne.get_column_names_from_dict(dict_with_table_rows={'Jaeger':'Gipsy Danger'})
        ['Jaeger']
        >>> ChallengerOne.get_column_names_from_dict(dict_with_table_rows={'Nr.': 123, 'E-Mail': 'x@y.z'})
        ['Nr', 'E_Mail']
        """
        field_names = list(dict_with_table_rows.keys())
        return [f.replace(".", "").replace("-", "_").strip() for f in field_names]

    def insert_data(self, list_of_dicts):
        for row_dict in list_of_dicts:
            self.insert_row_from_dict(row_dict)

    def insert_row_from_dict(self, dict_to_be_inserted):
        column_names = self.get_column_names_from_dict(dict_to_be_inserted)
        cursor = self.db.cursor()
        sql = "insert into PERSON (" + ', '.join(column_names) + ")" + \
            "values ('" + "', '".join(dict_to_be_inserted.values()) + "')"
        cursor.execute(sql)

    def work(self):
        data = self.read_data(r'C:\Users\eick036\repos\python-school\challenge\Testdaten_1.csv')
        self.create_database(data)
        self.insert_data(data)

    def shut_down(self):
        self.db.close()


if __name__ == '__main__':
    #c = ChallengerOne()
    #c.work()
    doctest.testmod()