from markov import MarkovTable
from random import Random

jsonFileName = 'chains_consonants.json'

seed = 1

with open(jsonFileName, "rb") as jsonFile:
    print "Loading JSON"
    markov = MarkovTable()
    markov.readJSON(jsonFile)
    print "JSON loaded"
    
print "Making words:\n"
rand = Random(seed)
for i in range(10):
    print markov.makeRandomWord(rand)

markov.removeTopLinks(0.01)

print "Making words:\n"
rand = Random(seed)
for i in range(10):
    print markov.makeRandomWord(rand)