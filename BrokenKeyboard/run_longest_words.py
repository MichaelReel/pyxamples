from time import time

input_01 = ("3\nabcd\nqwer\nhjklo")
input_02 = ("4\nedcf\nbnik\npoil\nvybu")

dictFile = 'enable1.txt'

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
                # Only update words if dictionary updated
                for k in range(len(inputArr)):
                    if key.issubset(inputArr[k]) and len(outputArr[k]) < len(w):
                        outputArr[k] = w
    
    for k in range(len(inputArr)):
        print "{} = {}".format(inputArr[k], outputArr[k])
        
    print "Time taken: {}".format(time() - startTime)
    
getLongestWords(input_01, dictFile)

getLongestWords(input_02, dictFile)