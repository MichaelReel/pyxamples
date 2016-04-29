from string import punctuation
import random
import re

sample_input = ("According to a research team at Cambridge University, "
                "it doesn't matter in what order the letters in a word are, "
                "the only important thing is that the first and last letter be in the right place. "
                "The rest can be a total mess and you can still read it without a problem. "
                "This is because the human mind does not read every letter by itself, but the word as a whole. "
                "Such a condition is appropriately called Typoglycemia.")

def typoword(s):
    """Takes a string and 'typoglycemates' it."""
    match = re.match(r"(.+)([\s" + punctuation + "])(.+)", s)
    if match:
        return typoword(match.group(1)) + match.group(2) + typoword(match.group(3))
    elif (len(s) > 2):
        return s[0] + ''.join(random.sample(s[1:-1], len(s)-2)) + s[-1:]
    else:
        return s

print typoword(sample_input)