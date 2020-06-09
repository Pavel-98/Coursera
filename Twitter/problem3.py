import sys
import json

sentimentItems = {}
TwitScores = {}



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
    numberOfWords = 0;
    points = 0
    otherWords = {}
    for word in wordsInText:
            if word in sentimentItems:
                points += sentimentItems[word]
                numberOfWords += 1
            else:
                numberOfWords += 1
                for otherWord in otherWords:
                    if otherWord == word:
                        otherWords[otherWord] += 1
                        break
                if not word in otherWords:
                    otherWords[word] = 1
    level = points / numberOfWords
    for twitScore in otherWords:
        if twitScore in TwitScores:
            TwitScores[twitScore] += level
        else:
            TwitScores[twitScore] = level
for twit in TwitScores.keys():
    print(twit + ' ' + str(TwitScores[twit]))


