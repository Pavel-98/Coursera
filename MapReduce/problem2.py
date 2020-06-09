import MapReduce
import json
import sys


def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(id, values):
    for value in values:
        if value[0] == "order":
            for value2 in values:
                if value2[0] == "line_item":
                    mr.emit(value + value2)

mr = MapReduce.MapReduce()
mr.execute(open(sys.argv[1], 'r'), mapper, reducer)
