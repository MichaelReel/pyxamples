from random import Random
from sys import maxint, path

print (path)

path.append("..\\Markov")

print (path)

from markov import MarkovTable

class Character(dict):

    markov = MarkovTable()
    with open("names_markov.json", "rb") as jsonFile:
        markov.readJSON(jsonFile)

    def __init__(self, seed):
        rand = Random(seed)
        self.createName(rand.randint(-maxint - 1, maxint))

    def createName(self, seed):
        rand = Random(seed)
        self['name'] = Character.markov.makeRandomWord(rand)




char = Character(1)
print (char)