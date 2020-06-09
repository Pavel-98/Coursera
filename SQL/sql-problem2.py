import psycopg2
import sys
conn = psycopg2.connect(dbname='database', user='postgres',
                        password='1', host='localhost')
cursor = conn.cursor()



cursor.execute('select a.row_num b.col_num, sum(a.value * b.value) where a.row_num = b.col_num group by a.row_num, b.col_num')
number = cursor.fetchone()
file = open("part_g.txt", "a")
file.write(str(number))