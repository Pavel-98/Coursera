import psycopg2
import sys
conn = psycopg2.connect(dbname='reuters', user='postgres',
                        password='1', host='localhost')
cursor = conn.cursor()



cursor.execute('select A.docid B.docid, sum(A.count * B.count) where A.docid = B.docid group by A.docid, '
               'B.docid')
number = cursor.fetchone()
file = open("part_h.txt", "a")
file.write(str(number))



cursor.execute(
               "create VIEW if not exists tempT as SELECT * FROM frequency UNION SELECT 'q' as docid, 'washington' as term, 1 as count  UNION SELECT 'q' as docid, 'taxes' as term, 1 as count UNION SELECT 'q' as docid, 'treasury' as term, 1 as count; " 
"select A.docid, B.docid, sum(A.count * B.count) as result from tempT A, tempT B on A.term = B.term where A.docid = 'q' and B.docid != 'q'")
number = cursor.fetchone()
file = open("part_i.txt", "a")
file.write(str(number))