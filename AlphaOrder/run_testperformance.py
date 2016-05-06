import time
import collections
from globals import *
import oneline
import failfast
import listcomps
import singlelistcomp

testFile = 'words.txt'

functionCalls = [ 
        oneline.alphorder, 
        failfast.alphorder, 
        listcomps.alphorder, 
        singlelistcomp.alphorder, 
    ]

result = collections.namedtuple('Results', ['ordered', 'reversed', 'unordered'])

def findOrderedWords(fun, filename):
    ordered = 0
    reversed = 0
    unordered = 0
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            res1 = fun(line)
            if (res1 == inOrder):
                ordered += 1
            elif (res1 == revOrder):
                reversed += 1
            else:
                unordered += 1
    return result(ordered, reversed, unordered)
    
for funct in functionCalls:
    start = time.time()
    results = findOrderedWords(funct, testFile)
    runtime = time.time() - start
    print '{}, runtime: {}, {}'.format(results, runtime, funct.__doc__)