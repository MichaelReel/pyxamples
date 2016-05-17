import random

class Tree():
    def __init__(self):
        self.g = None
        self.G = None
        self.code = None
        
    def __str__(self):
        left = self.g if self.g else ""
        data = self.code if self.code else ":g  <->  G:"
        right = self.G if self.G else ""
        return "({}{}{})".format(left, data, right)
    
    def str_tree(self, prefix=""):
        result = ""
        if self.g:
            result += self.g.str_tree(prefix + "   |") + "\n"
            result += prefix + " g:/\n"
        if self.code:
            result += (prefix + "<" + self.code + ">") + ("\n" if self.G else "")
        if self.G:
            result += prefix + " G:\\"
            result += "\n" + self.G.str_tree(prefix + "   |")
        return result
        
    def addKey(self, gs, eng):
        if not gs:
            self.code = eng
            return
        if getattr(self, gs[0]) == None:
            setattr(self, gs[0], Tree())
        side = getattr(self, gs[0])
        side.addKey(gs[1:], eng)
        
    def nextKey(self, gs):
        """returns a tuple (key, value) off the front of the string"""
        if not hasattr(self, gs[0]):
            return ('', self.code) if self.code else (gs[0], gs[0])
        if getattr(self, gs[0]) == None:
            return ('', self.code)
        else:
            res = getattr(self, gs[0]).nextKey(gs[1:])
            return (gs[0] + res[0], res[1])
        
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