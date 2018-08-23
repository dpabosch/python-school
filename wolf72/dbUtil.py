import cx_Oracle
import sys
import os

print(os.environ['PYTHONPATH'])
print('arg='+sys.argv[1])


#con = cx_Oracle.connect('APPSOLAR_SCHEMA/DEVSOLAR@localhost/SOLDEV')
con = cx_Oracle.connect('APPSOLAR_DMD/CKUUSJYH@GTLDPATEST0002.dpa.bagint.com:1400/SOLTEST2')
puffer_status = ['inBearbeitung']

cur = con.cursor()
cur.execute('select count(1) anz, datenquelle from dmd_anschriftpuffer where pufferstatus in (\''+','.join(puffer_status)+'\') group by datenquelle')
for result in cur:
    print(result)

cur.close()
con.close()
