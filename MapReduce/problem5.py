import MapReduce
import json
import sys

def mapper(record):
    mr.emit_intermediate(record[1][0:-10:1], record[0])

def reducer(id, values):
    mr.emit(id)
    return

mr = MapReduce.MapReduce()
mr.execute(open(sys.argv[1], 'r'), mapper, reducer)