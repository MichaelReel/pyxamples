from alien_keytree import Tree
from string import punctuation
import re

in_let = "A grand new statement, trying to encode with new vars, etc."

def encode (in_let):
    letters = ''.join(set(re.sub("[" + punctuation + " ]", "", in_let)))
    root = Tree()
    for c in letters:
        root.pushKey(c)
    key = root.getPrintKeys()
    test = root.encode(in_let)
    
    print key
    print test
    
    decoder = Tree(key)
    print decoder.decode(test)

encode(in_let)