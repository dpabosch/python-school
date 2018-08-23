import sqlite3
import mstahl.huhn.huhnparser as hp

def convert_merkmal_to_column(merkmal):
    return merkmal.lower().replace(' ','_')


def create_huhn_db(huehner):
    columns = " varchar(255),".join((convert_merkmal_to_column(merkmal) for merkmal in huehner[0].merkmale.keys()))
    create_huhn_table_str = """CREATE TABLE if not exists rasse (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,{})""".format(columns)
    print(create_huhn_table_str)
    with sqlite3.connect('huhn.db') as con:
        con.execute(create_huhn_table_str)

def insert_huhn(huehner):
    with sqlite3.connect('huhn.db') as con:
        c = con.cursor()
        for huhn in huehner:
            column_names = ",".join(convert_merkmal_to_column(merkmal) for merkmal in huhn.merkmale.keys())
            huhn_merkmale = ",".join("'{}'".format(value) for value in huhn.merkmale.values())
            insert_String = """INSERT INTO rasse ({}) VALUES ({});""".format(column_names, huhn_merkmale)
            print(insert_String)
            c.execute(insert_String)
        con.commit()
        c.execute("SELECT * FROM rasse")
        for row in c.fetchall():
            print(row)
        c.close()

def check_if_exists():
    with sqlite3.connect('huhn.db') as con:
        con.execute("SELECT id FROM rasse WHERE id = 1")

def main():
    try:
        check_if_exists()
    except sqlite3.OperationalError:
        website = 'https://de.wikipedia.org/wiki/Liste_von_H%C3%BChnerrassen'
        wikitable = hp.parse_huhn_table_from(website)
        huehner_mit_merkmalen = hp.parse_merkmale_from(wikitable)
        huehner = hp.get_huhn_mit_min_legeleistung(huehner_mit_merkmalen, 0)
        create_huhn_db(huehner)
        insert_huhn(huehner)

if __name__ == "__main__":
    main()
