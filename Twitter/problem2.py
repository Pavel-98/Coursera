import json
import sys
sentimentItems = {}



afinnfile = open(sys.argv[1], 'r')
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  sentimentItems[term] = int(score)  # Convert the score to an integer.

 # Print every (term, score) pair in the dictionary

file = open(sys.argv[2], 'r')

for record in file:
    jsRec = json.loads(record)
    if not 'text' in record:
        continue
    text = jsRec['text']
    wordsInText = text.split(' ')

    points = 0

    for word in wordsInText:
        if word in sentimentItems:
            points += sentimentItems[word]
    print(points)


