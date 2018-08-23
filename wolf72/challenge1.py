import cx_Oracle
import csv
import re


def read_csv(filename, encoding='UTF-8', delimiter=';'):
    contentList = []
    headerList=[]
    try:
        header=True
        with open(filename, encoding=encoding) as csvfile:
            #csvData = csv.DictReader(csvfile, skipinitialspace=True, delimiter=delimiter)#
            rows = csvfile.readlines()
            for row in rows:
                rowData=row.split(delimiter)
                if header:
                    for field in rowData:
                        headerList.append(field.strip().lower())
                    header=False
                else:
                    for dataCell in rowData:
                        contentList.append(dataCell.strip())
    except FileNotFoundError:
        print('Datei konnte nicht gefunden werden.')
    return headerList, contentList

headerList,contentList=read_csv('../challenge/Testdaten_1.csv', 'Windows-1252')

for content in headerList:
    print(content)

con = cx_Oracle.connect('APPSOLAR_SCHEMA/DEVSOLAR@localhost/SOLDEV')
#con = cx_Oracle.connect('APPSOLAR_DMD/CKUUSJYH@GTLDPATEST0002.dpa.bagint.com:1400/SOLTEST2')

cur = con.cursor()
cur.execute('drop table person')
cur.execute('create table person('
            'anrede VARCHAR2(64), '
            'titel VARCHAR2(64),'
            'vorname VARCHAR2(64),'
            'nachname VARCHAR2(64),'
            'geburtsdatum VARCHAR2(64))')

for content in contentList:
    print(content)
    cur.execute('insert into person(anrede, titel, vorname, nachname, geburtsdatum) values('
                '\''+contentList[headerList.index("anrede")]+'\', '
                '\''+contentList[headerList.index("titel")]+'\', '
                '\''+contentList[headerList.index("vorname")]+'\', '
                '\''+contentList[headerList.index("nachname")]+'\', '
                '\''+contentList[headerList.index("geburtsdatum")]+'\')')

# cur.execute('select count(1) anz, datenquelle from dmd_anschriftpuffer where pufferstatus in (\''+','.join(puffer_status)+'\') group by datenquelle')
#for result in cur:
#    print(result)

cur.close()
con.close()
