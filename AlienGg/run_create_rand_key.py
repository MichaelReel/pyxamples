import random
from alien_keytree import Tree

in_let = "Helowrd"

letters = ''.join(random.sample(in_let, len(in_let)))
root = Tree()
for c in letters:
    root.pushKey(c)
root.printKeys()

