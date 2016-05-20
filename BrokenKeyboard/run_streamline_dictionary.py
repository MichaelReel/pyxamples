from collections import deque
from time import time
import sys

dictFile    = 'enable1.txt'
newDictFile = 'enable2.txt'

def getBestWord(letters, dictionary):
    bestWord = ""
    for word in dictionary:
        word = word.strip()
        if set(word).issubset(set(letters)) and len(bestWord) < len(word):
            bestWord = word
    return bestWord

def streamLineDictionary(inFile, outFile):
    startTime = time()
    
    # Read all the words into memory
    inWordList = deque()
    swapDeque = deque()
    outWordList = []
    
    with open(inFile) as words:
        for w in words:
            inWordList.append(w.strip())
    print "Words Read. Total time so far: {}".format(time() - startTime)
    
    # Remove words that are subset
    letter = "  "
    while inWordList:
        word = inWordList.popleft()
        # Debug
        if word[:2] != letter:
            letter = word[:2]
            print "{} words started @ {}".format(letter, time() - startTime)
            print "{} words left in list {} kept in new list".format(len(inWordList), len(outWordList))
            sys.stdout.flush()
        
        # Test against every other word in the list
        while inWordList:
            iw = inWordList.popleft()
            if set(iw) == set(word) and len(word) < len(iw):
                    # This iword has the same letters and is longer than the current word
                    # Don't save the current word, just proceed with the "better" word
                    word = iw
            else:
                # No relation to this word. Pop it back onto the list
                swapDeque.append(iw)
        
        # Stick the "best" word on the output list and Swap the buffer
        outWordList.append(word)
        inWordList = swapDeque
        swapDeque = deque()
        
    print "Stripping complete. Total time so far: {}".format(time() - startTime)
    
    outList = sorted(outWordList)
    print "Sorting complete. Total time so far: {}".format(time() - startTime)
    
    # Write out streamlined list to file
    with open(outFile, "w+") as newDict:
        for word in outWordList:
            newDist.write(word)
            newDist.write("\n")
    print "Output written. Total time taken: {}".format(time() - startTime)

streamLineDictionary(dictFile, newDictFile)