import time

input_01 = ("3\nabcd\nqwer\nhjklo")
input_02 = ("4\nedcf\nbnik\npoil\nvybu")

dictFile = 'enable1.txt'

def getLongestWords(inputStr, dictFile):
    inputArr = inputStr.split("\n");
    outputArr = ["" for x in range(int(inputArr.pop(0)))]
    
    with open(dictFile) as df:
        for word in df.readlines():
            word = word.strip()
            for k in range(len(inputArr)):
                if set(word).issubset(set(inputArr[k])) and (len(outputArr[k]) < len(word)):
                    outputArr[k] = word
    
    for k in range(len(inputArr)):
        print "{} = {}".format(inputArr[k], outputArr[k])
    
startTime = time.time()
getLongestWords(input_01, dictFile)
print "Time taken: {}".format(time.time() - startTime)

startTime = time.time()
getLongestWords(input_02, dictFile)
print "Time taken: {}".format(time.time() - startTime)