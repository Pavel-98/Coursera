import psycopg2
import sys
conn = psycopg2.connect(dbname='database', user='postgres',
                        password='1', host='localhost')
cursor = conn.cursor()



cursor.execute('select count(*) from (select * from frequncy where docid=\'10398_txt_earn\') x')
number = cursor.fetchone()
file = open("part_a.txt", "a")
file.write(str(number))



cursor.execute('select count(*) from (select * from frequency where docid=\'10398_txt_earn\' and count = 1) x')
number = cursor.fetchone()
file = open("part_b.txt", "a")
file.write(str(number))



cursor.execute('select count(*) from (select * from frequency where docid=\'10398_txt_earn\' and count = 1 union select * '
               'from frequency where docid = \'925_txt_trade\' and count = 1) x')
number = cursor.fetchone()
file = open("part_c.txt", "a")
file.write(str(number))



cursor.execute('select count(*) from (select distinct * from frequency where term like \'%law%\' or term like \'%legal%\') x')
number = cursor.fetchone()
file = open("part_d.txt", "a")
file.write(str(number))



cursor.execute('select count(*) from (select docid, count(term) as c from frequency group by docid having c > 300)')
number = cursor.fetchone()
file = open("part_e.txt", "a")
file.write(str(number))



cursor.execute('select count(*) from (select distinct * from frequency where docid like \'%transaction%\' and docid like '
               '\'%world%\') x')
number = cursor.fetchone()
file = open("part_f.txt", "a")
file.write(str(number))