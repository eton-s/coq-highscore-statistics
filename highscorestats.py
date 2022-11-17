import json
import numpy
import scipy
with open('HighScores.json') as json_file:
    data = json.load(json_file)
    print("----------------------------")
    print("|CoQ High Score Statistics |")
    print("----------------------------")
    n = 0
    scores = []
    turns = []
    levels = []
    gamemodes = []
    for run in data["Scores"]: # read in runs
        n += 1
        scores += [run["Score"]]
        turns += [run["Turns"]]
        levels += [run["Level"]]
    # print results
    print("#runs:           | " + str(n))
    print("----------------------------")
    print("high score:      | " + str(max(scores)))
    print("----------------------------")
    print("avg level:       | " + str(sum(levels)/n))
    print("median level:    | " + str(numpy.median(levels)))
    print("highest level:   | " + str(numpy.partition(numpy.asarray(levels), n-1)[n-1]))
    print("-----Level Distribution-----")
    for i in range(10):
        n = 0
        for r in levels:
            if r >= i*5 and r < (i+1)*5:
                n += 1
        print("{}-{}            | ".format(str(i*5).rjust(2, '0'), str((i+1)*5-1).rjust(2, '0')) + str(n))
    for r in levels:
        if r >= 50:
            n += 1
    print("50+              | ".format(str(i*5).rjust(2, '0'), str((i+1)*5).rjust(2, '0')) + str(n))
        