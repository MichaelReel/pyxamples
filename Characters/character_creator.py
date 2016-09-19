from random import Random
from sys import maxint, path
path.append("..\\Markov")
from markov import MarkovTable

class Character(dict):

    markovForenames = MarkovTable()
    with open("markov_tables/forenames_3.json", "rb") as jsonFile:
        markovForenames.readJSON(jsonFile)
        
    markovSurnames = MarkovTable()
    with open("markov_tables/surnames_3.json", "rb") as jsonFile:
        markovSurnames.readJSON(jsonFile)

    def __init__(self, seed):
        rand = Random(seed)
        self.createName(rand.randint(-maxint - 1, maxint))
        self.createAppearance(rand.randint(-maxint - 1, maxint))

    def createName(self, seed):
        rand = Random(seed)
        self['forename'] = Character.markovForenames.makeRandomWord(rand).strip()
        self['surname'] = Character.markovSurnames.makeRandomWord(rand).strip()

    def createAppearance(self, seed):
        rand = Random(seed)
        self['stature'] = ( rand.choice(['short ', '', 'tall ']) +
                            rand.choice(['thin ', '', 'broad ']) ).strip()
        self['hair'] = ( rand.choice(['balding ', 'cropped ', 'short ', 'eye-length ', 'neck-length ', 'shoulder-length ', 'waist-length ', '']) +
                         rand.choice(['tight-curled ', 'curly ', 'wavy ', 'straight ', '']) +
                         rand.choice(['white ', 'grey ', 'blond ', 'fair ', 'red ', 'light brown ', 'brown ', 'dark brown ', 'black ', '']) ).strip()
        self['eyes'] = ( rand.choice(['brown ', 'hazel ', 'blue ', 'green ', 'grey ', 'amber ', 'black ', 'pink ']) +
                         rand.choice(['', 'wide', 'sad', 'clear', 'happy', 'narrow'])).strip()

    def __str__(self):

        return ("---------------------------------------------------\n"
               "{forename} {surname}\n"
               "----------------------------------------------------\n"
               "{stature}\n"
               "{hair} hair\n"
               "{eyes} eyes\n"
               "").format(**self)


chars = [Character(x) for x in range(10)]
for char in chars:
    print (char)