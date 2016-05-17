import random

class Tree():
    def __init__(self, key=""):
        self.g = None
        self.G = None
        self.code = None
        list_key = key.split(' ')
        for k, v in zip(list_key[1::2], list_key[::2]):
            self.addKey(k, v)
        
    def __str__(self):
        left = self.g if self.g else ""
        data = self.code if self.code else ":g  <->  G:"
        right = self.G if self.G else ""
        return "({}{}{})".format(left, data, right)
    
    def str_tree(self, prefix=""):
        result = ""
        if self.g:
            result += self.g.str_tree(prefix + "   /") + "\n"
            result += prefix + " g:/\n"
        if self.code:
            result += (prefix + "<" + self.code + ">") + ("\n" if self.G else "")
        if self.G:
            result += prefix + " G:\\"
            result += "\n" + self.G.str_tree(prefix + "   \\")
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
                
    def getPrintKeys(self, precode=""):
        printKey = ""
        if self.g:
            printKey += self.g.getPrintKeys(precode + 'g')
        if self.code:
            printKey += self.code + " " + precode + " "
        if self.G:
            printKey += self.G.getPrintKeys(precode + 'G')
        return printKey
    
    def encode(self, plain_str):
        # create a map table
        list_key = self.getPrintKeys().split()
        trans_table = {}
        for k, v in zip(list_key[1::2], list_key[::2]):
            trans_table[v] = k
        encoded_str = ""
        for i in plain_str:
            encoded_str += trans_table[i] if i in trans_table else i
        return encoded_str
    
    def decode(self, subject):
        gs = subject
        translation = ""
        while gs:
            res = self.nextKey(gs)
            gs = gs[len(res[0]):]
            translation += res[1]
        return translation
    