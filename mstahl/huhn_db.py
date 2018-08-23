import sqlite3
import mstahl.huhn.huhnparser as hp

def convert_merkmal_to_column(merkmal):
    return merkmal.lower().replace(' ','_')

website = 'https://de.wikipedia.org/wiki/Liste_von_H%C3%BChnerrassen'

huehner = hp.get_huhn_mit_min_legeleistung(hp.parse_merkmale_from(hp.parse_huhn_table_from(website)),0)

columns = " STRING,".join((convert_merkmal_to_column(merkmal) for merkmal in huehner[0].merkmale.keys()))

create_huhn_table_str = """CREATE TABLE rasse (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,{})""".format(columns)

print (create_huhn_table_str)



con = sqlite3.connect('huhn.db')
con.execute(create_huhn_table_str)
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
con.close()