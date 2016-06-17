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
    print ' '.join( repeat("meh", 4) )
    # meh meh meh meh

# Iterators terminating in the shortest input sequence:

def chain_ex():
    # Exhausts all iterables in sequence
    print ' '.join( chain('ab', 'cd', 'ef') )
    # a b c d e f

    print ' '.join( chain.from_iterable(['ab', 'cd', 'ef']) )
    # a b c d e f

def compress_ex():
    # Filter elements from data returning only those that have a corresponding
    # selector that evaluates to True
    print ' '.join( compress('ABCDEF', [1,0,1,0,1,1]) )
    # A C E F

def dropwhile_ex():
    # Drop elemtents while predicate is True, after return all elements
    for i in dropwhile(lambda x: x<5, [1, 4, 6, 4, 1]):
        print i
        # 6
        # 4
        # 1

def groupby_ex():
    # Return consecutive keys and groups from the iterable
    print ' '.join( [k for k, g in groupby('AAAABBBCCDAABBB')] )
    # A B C D A B

    for group in [list(g) for k, g in groupby('AAAABBBCCDAABBB')]:
        print group
        # ['A', 'A', 'A', 'A']
        # ['B', 'B', 'B']
        # ['C', 'C']
        # ['D']
        # ['A', 'A'] 
        # ['B', 'B', 'B']
        
    for t in  [(k, list(g)) for k, g in groupby('AAAABBBCCDAABBB')]:
        print t
        # ('A', ['A', 'A', 'A', 'A'])
        # ('B', ['B', 'B', 'B'])
        # ('C', ['C', 'C']) 
        # ('D', ['D'])
        # ('A', ['A', 'A'])
        # ('B', ['B', 'B', 'B'])

def ifilter_ex():
    # Filter elements from iterator using predicate, pass true
    print ' '.join( str(x) for x in ifilter(lambda x: x % 2, range(10)) )
    # 1 3 5 7 9

    print ' '.join( ifilter(lambda ch: ord(ch) & 2, 'abcdefghijklmnopqrstuvwxyz') )
    # b c f g j k n o r s v w z

def ifilterfalse_ex():
    # Filter elements from iterator using predicate, pass False
    print ' '.join( str(x) for x in ifilterfalse(lambda x: x % 2, range(10)) )
    # 0 2 4 6 8

    print ' '.join( ifilterfalse(lambda ch: ord(ch) & 2, 'abcdefghijklmnopqrstuvwxyz') )
    # a d e h i l m p q t u x y

def islice_ex():
    # Returns selected elements from iterable depending on start, stop and step
    # If start is non-zero the skip until start is reached
    # If stop is None, continue to end, else stop at specified point
    # If step is higher than one, then skip elements
    print ' '.join( islice('ABCDEFG', 2)          )              # A B
    print ' '.join( islice('ABCDEFG', 2, 4)       )              # C D
    print ' '.join( islice('ABCDEFG', 2, None)    )              # C D E F G
    print ' '.join( islice('ABCDEFG', 0, None, 2) )              # A C E G


# count_ex()
# cycle_ex()
# repeat_ex()
# chain_ex()
# compress_ex()
# dropwhile_ex()
# groupby_ex()
# ifilter_ex()
# ifilterfalse_ex()
# islice_ex()