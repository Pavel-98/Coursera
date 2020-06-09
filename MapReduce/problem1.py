import MapReduce
import json
import sys




def mapper(book):
    for word in book[1].split():
        mr.emit_intermediate(word, book[0])

def reducer(id, values):
    list = []
    for value in values:
        if value not in list:
            list.append(value)
    mr.emit((id, list))
mr = MapReduce.MapReduce()
mr.execute(open(sys.argv[1], 'r'), mapper, reducer)