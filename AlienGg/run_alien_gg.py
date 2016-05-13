
hw_key = "H GgG d gGg e ggG l GGg o gGG r Ggg w ggg a gG"
hw_test = "GgGggGGGgGGggGG, ggggGGGggGGggGg!"

real_key = "C GgggGgg H GgggGgG T GgggGGg a gGg c GGggG d GggG e GgG g ggGgG h GGgGg i gGGg j GgggGGG l gGGG m ggGGg n GGgGG o ggg p ggGGG r GGGg s GGGG t GGgggG u ggGgg v Ggggg w GGggggg y GGggggG"
real_test = "GgggGGgGGgGggGGgGGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG GGggggggGgGGGG ggGGGGGGggggggGGGgggGGGGGgGGggG gGgGGgGGGggG GggGgGGgGGGGGGggGggGggGGGGGGGGGgGGggG gggGggggGgGGGGg gGgGGgggG /GGGg/GggGgGggGGggGGGGGggggGggGGGGGGggggggGgGGGGggGgggGGgggGGgGgGGGGg_gGGgGggGGgGgGgGGGG. GgggGgGgGgGggggGgG gGg GGggGgggggggGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG gGGgGggGGgGgGg? GgggGgggggggGGgGgG GgggGGGggggGGgGGgGG ggGggGGGG gggGggggGgGGGGg GGgggGGGgGgGgGGGGgGgG!"

pbreen_key = "D GgggGgg p gGGg d GgggGGg y gGg o GGggG h ggGgG i GGgGg a GgggGgG s GgggGGG c GgG r GggG"
pbreen_test = "GgggGggGgggGgGGgggGGgGgggGGggGg GGggGGggG GgGggGgGGGgGggGGgGgggGGG?"

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
    
def decode(key, subject):
    root = Tree()
    list_key = key.split(' ')
    for k, v in zip(list_key[1::2], list_key[::2]):
        root.addKey(k, v)
    # print root
    print root.str_tree()
    
    gs = subject
    translation = ''
    while gs:
        res = root.nextKey(gs)
        gs = gs[len(res[0]):]
        translation += res[1]
        
    print translation
        
decode(hw_key, hw_test)
# decode(real_key, real_test)
# decode(pbreen_key, pbreen_test)