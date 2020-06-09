import json
import sys



tags = {}

def topTen():
    fileres = open('data', 'r')
    for record in fileres:
        recTweet = json.loads(record)
        for hashtag in recTweet['entities']['hashtags']:

                text = hashtag['text']
                if text not in tags:
                    tags[text] = 1
                else:
                     tags[text] = tags[text] + 1

    l = list(tags.items())
    l.sort(key = lambda x: x[1])

    i = 0

    for id in l:
        print(str(id[0]) + ' ' + str(id[1]))
        i += 1
        if i == 10:
            break

def main():
    topTen()

main()