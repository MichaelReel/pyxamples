import time, sys

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
    startTime = time.time()
    with open(inFile) as words, open(inFile) as dict, open (outFile, "w+") as newDict:
        lineCount = sum(1 for line in dict)
        line001Pct = lineCount / 1000
        print "{} total lines to read.".format(lineCount)
        sys.stdout.flush()
        linesRead = 0
        progress = 0
        for iw in words:
            iw = iw.strip()
            dict.seek(0)
            if len(getBestWord(iw, dict)) <= len(iw):
                newDict.write(iw)
                newDict.write('\n')
            linesRead += 1
            newProg = linesRead / line001Pct
            if newProg > progress:
                progress = newProg
                print "{} lines, {}% file read, {}s so far".format(linesRead, float(progress) / 10, time.time() - startTime)
                sys.stdout.flush()
    print "Time taken: {}".format(time.time() - startTime)

streamLineDictionary(dictFile, newDictFile)