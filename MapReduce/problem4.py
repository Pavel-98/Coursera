import MapReduce
import json
import sys

def mapper(record):
    mr.emit_intermediate(record[0], record)
    mr.emit_intermediate(record[1], record)
def reducer(id, values):
     for value in values:
         if [value[1], value[0]] not in values:
             if value[0] == id:
                 mr.emit((id, value[1]))
             else:
                 mr.emit((value[0], id))


mr = MapReduce.MapReduce()
mr.execute(open(sys.argv[1], 'r'), mapper, reducer)