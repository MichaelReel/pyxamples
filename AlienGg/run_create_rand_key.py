import random

in_let = "Helowrd"

class Tree():
    def __init__(self):
        self.g = None
        self.G = None
        self.code = None

    def pushKey(self, letter):
        if not self.g or not self.G:
            if not self.code:
                self.code = letter
                return
            else:
                self.g = Tree()
                self.g.pushKey(self.code)
                self.code = None
                self.G = Tree()
                self.G.pushKey(letter)
        else:
            #push to a random path
            if (random.random() < 0.5):
                self.g.pushKey(letter)
            else:
                self.G.pushKey(letter)
                
    def printKeys(self, precode=""):
        if self.g:
            self.g.printKeys(precode + 'g')
        if self.code:
            print self.code + " " + precode + " "
        if self.G:
            self.G.printKeys(precode + 'G')

letters = ''.join(random.sample(in_let, len(in_let)))
root = Tree()
for c in letters:
    root.pushKey(c)
root.printKeys()

