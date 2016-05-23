from time import time
from itertools import combinations

input_01 = ("3\nabcd\nqwer\nhjklo")
input_02 = ("4\nedcf\nbnik\npoil\nvybu")

dictFile = 'enable1.txt'

def getSubsets(s):
    res = []
    for i in range(1, len(s) + 1):
        for combo in combinations(s, i):
            res.append(frozenset(combo))
    return res

def getLongestWords(inputStr, dictFile):
    startTime = time()
        
    inputArr = inputStr.split("\n");
    outputArr = ["" for x in range(int(inputArr.pop(0)))]
    
    wordDict = {}
    
    with open(dictFile) as words:
        for w in words:
            w = w.strip()
            key = frozenset(w)
            if not key in wordDict or len(wordDict[key]) < len(w):
                wordDict[key] = w

    for k in range(len(inputArr)):
        for key in getSubsets(frozenset(inputArr[k])):
            if key in wordDict and len(wordDict[key]) > len(outputArr[k]):
                outputArr[k] = wordDict[key]
    
    for k in range(len(inputArr)):
        print "{} = {}".format(inputArr[k], outputArr[k])
        
    print "Time taken: {}".format(time() - startTime)

getLongestWords(input_01, dictFile)

getLongestWords(input_02, dictFile)