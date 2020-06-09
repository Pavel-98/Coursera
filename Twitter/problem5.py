import json
import sys
sentimentItems = {}
scoresForCountries = {}
numberForCountries = {}
avg = {}
afinnfile = open(sys.argv[1])
scores = {} # initiaize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    sentimentItems[term] = int(score)  # Convert the score to an integer.

 # Print every (term, score) pair in the dictionary

file = open(sys.argv[2], 'r')

for record in file:
    jsRec = json.loads(record)
    if not 'text' in jsRec or not 'place' in jsRec:
        continue
    text = jsRec['text']
    if jsRec['place'] == None:
        continue
    placeCode = jsRec['place']['full_name']
    state = jsRec['place']['country_code']
    if placeCode != "US":
        continue
    wordsInText = text.split()
    points = 0
    number = 0
    for word in wordsInText:
        number += 1
        if word in sentimentItems:
            points += sentimentItems[word]
    average = points / number
    if state in scoresForCountries:
        scoresForCountries[state] += points
    else:
        scoresForCountries[state] = points
    if state in numberForCountries:
        numberForCountries[state] += number
    else:
        numberForCountries[state] = number
for state in numberForCountries:
    avg[state] = scoresForCountries[state] / numberForCountries[state]
res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
print(res)