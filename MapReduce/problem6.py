import MapReduce
import json
import sys



def mapper(record):

    if record[0] == 'a':
        i = 0
        while i < 5:
            mr.emit_intermediate(str(record[1]) + ' ' + str(i), record)
            i = i + 1
    if record[0] == 'b':
        i = 0
        while i < 5:
            mr.emit_intermediate(str(i) + ' ' + str(record[2]), record)
            i = i + 1

def reducer(id, values):
    res = 0

    for value in values:
        for value2 in values:
            if value[0] == 'a':
                if value[2] == value2[1] and value2[0] == 'b':
                    res += value[-1] * value2[-1]
    mr.emit((int(list(id)[0]), int(list(id)[2]), res))

mr = MapReduce.MapReduce()
mr.execute(open(sys.argv[1], 'r'), mapper, reducer)