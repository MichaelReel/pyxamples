from markov import MarkovTable
from random import Random

csvFileName = 'chains_2letter.csv'
seed = 1

with open(csvFileName, "rb") as csvFile:
    print "Loading csv"
    markov = MarkovTable(csvFile=csvFile)
    print "CSV loaded"

print "Making words:"
rand = Random(seed)
for i in range(100):
    print markov.makeRandomWord(rand)