import json
import sys
import MapReduce


def mapper(record):
    mr.emit_intermediate(record[0], record[1])



def reducer(id, values):
    mr.emit((id, len(values)))



mr = MapReduce.MapReduce()


mr.execute(open(sys.argv[1], 'r'), mapper, reducer)