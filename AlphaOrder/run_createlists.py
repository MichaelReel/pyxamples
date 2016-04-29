import time
from globals import *
from failfast import alphorder

inputFile = 'words.txt'
orderOutput = 'orderedWords.log'
revOutput = 'reversedWords.log'

with open(inputFile) as inf, open(orderOutput, 'w+') as ordf, open(revOutput, 'w+') as revf:
    for line in inf.readlines():
        line = line.strip()
        result = alphorder(line)
        if (result == inOrder):
            ordf.write(line)
            ordf.write('\n')
        elif (result == revOrder):
            revf.write(line)
            revf.write('\n')
            

