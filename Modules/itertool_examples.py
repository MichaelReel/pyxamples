from itertools import *

# Samples based on descriptions at https://docs.python.org/2/library/itertools.html

# Infinite Iterators:

def count_ex():
    # count will continue to produce values infinitely
    for i in count(10, 2):
        print i
        # 10 12 14 16 18 20
        if i == 20:
            break

def cycle_ex():
    # cycle returns elements from an interable/list repeatedly
    b = 0
    for c in cycle('ABCD'):
        print c
        # A B C D A B C D A B
        if b >= 9:
            break
        else:
            b += 1

def repeat_ex():
    # Repeat will return the same element indefinitely, or up to n times
    for e in repeat("meh", 4):
        print e
        # meh meh meh meh

# count_ex()
# cycle_ex()
# repeat_ex()