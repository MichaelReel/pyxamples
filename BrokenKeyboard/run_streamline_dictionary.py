from collections import deque
from time import time
import sys

dictFile    = 'enable1.txt'
newDictFile = 'enable2.txt'

def streamLineDictionary(inFile, outFile):
    startTime = time()
    wordDict = {}
    
    with open(inFile) as words:
        for w in words:
            w = w.strip()
            key = frozenset(w)
            if not key in wordDict or len(wordDict[key]) < len(w):
                wordDict[key] = w

    print "Stripping complete. Total time so far: {}".format(time() - startTime)
    
    outList = sorted(wordDict.values())
    print "Sorting complete. Total time so far: {}".format(time() - startTime)
    
    # Write out streamlined list to file
    with open(outFile, "w+") as newDict:
        for word in outList:
            newDict.write(word)
            newDict.write("\n")
            
    print "Output written. Total time taken: {}".format(time() - startTime)

streamLineDictionary(dictFile, newDictFile)