#from oneline import alphorder
from failfast import alphorder
#from listcomps import alphorder
#from singlelistcomp import alphorder

inputFile = 'shortwords.txt'

with open(inputFile) as inf:
    for line in inf.readlines():
        line = line.strip()
        result = alphorder(line)
        print line, result