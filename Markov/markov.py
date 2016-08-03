from random import Random
import csv, re

vowels     = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

class MarkovTable(object):
    
    def __init__(self, csvFile = None, input = None, split = '1letter'):
        '''
        Create the markov chain table.
        By default the table will be empty.

        Setting csvFile will attempt to read the markov data 
        from a comma separated file handle. The file should 
        have already been opened for reading.

        Setting input will attempt to create markov data from 
        calling readLine on the given input.

        When input is given, split will determine the technique
        used to split words into markov states.
        split = '1letter' : 1 letter equals 1 state.
        split = '2letter' : Every 2 letters equals 1 state, 
                            last state may be a single letter.
        split = '3letter' : Every 3 letters equals 1 state, 
                            last state may be a single letter
                            or 2 letters. This can create a 
                            very large table.
        '''
        self.links = {}
        self.totals = {}
        self.headers = set()
        if csvFile:
            self.readCSV(csvFile)
        if input:
            self.readInputStream(input, split)

    def readInputStream(self, input, split):
        for line in input.readlines():
            line = line.strip()
            self.insertWord(line, split)

    def insertWord(self, word, split):
        commands = {
                '1letter'    : lambda x: self.splitLetter(x),
                '2letter'    : lambda x: self.splitMultiLetter(x, 2),
                '3letter'    : lambda x: self.splitMultiLetter(x, 3),
                'consonants' : lambda x: self.splitByRegex(x, "([aeiou]*[bcdfghjklmnpqrstvwxyz]{1})"),
            }
        try:
            return commands[split](word)
        except KeyError as e:
            print "KeyError caused by invalid split command '{}', valid commands are: {}".format(split, commands.keys())
            raise e
    
    def splitLetter(self, word):
        self.addLink(' ', word[0])
        self.addLink(word[-1], ' ')
        for a, b in zip(word, word[1:]):
            self.addLink(a, b)
    
    def splitMultiLetter(self, word_in, n):
        word = [word_in[i:i+n] for i in range(0, len(word_in), n)]
        self.addLink(' ', word[0])
        self.addLink(word[-1], ' ')
        for a, b in zip(word, word[1:]):
            self.addLink(a, b)

    def splitByRegex(self, word_in, regex):
        word = filter(None, re.split(regex, word_in))
        self.addLink(' ', word[0])
        self.addLink(word[-1], ' ')
        for a, b in zip(word, word[1:]):
            self.addLink(a, b)

    def addLink(self, start, end):
        self.headers.add(start)
        self.headers.add(end)
        if start not in self.links:
            self.links[start] = {}
            self.totals[start] = 0
        if end not in self.links[start]:
            self.links[start][end] = 0
        self.links[start][end] += 1
        self.totals[start] += 1

    def __str__(self):
        return str(self.links)

    def makeRandomWord(self, rand):
        # Use space to find a starting state:
        state = self.getRandomLinkedState(' ', rand)
        word = state
        while state != ' ':
            state = self.getRandomLinkedState(state, rand)
            word += state
        return word
        
    def getRandomLinkedState(self, state, rand):
        pos = rand.randint(0, self.totals[state])
        for nextState in self.links[state].keys():
            pos -= self.links[state][nextState]
            if pos < 0:
                return nextState

    def writeCSV(self, file):
        writer = csv.writer(file)
        headers = sorted(self.headers)
        writer.writerow([''] + headers)
        for key in headers:
            row = [key]
            for title in headers:
                if title in self.links[key].keys():
                    row += [self.links[key][title]]
                else:
                    row += [0]
            writer.writerow(row)

    def readCSV(self, file):
        reader = csv.DictReader(file)
        self.headers = sorted(reader.fieldnames)
        self.headers.remove('')

        for line in reader:
            rowState = line['']
            rowLinks = {}
            rowTotal = 0
            for header in self.headers:
                if line[header] > 0:
                    linkCount = int(line[header])
                    rowLinks[header] = linkCount
                    rowTotal += linkCount
            self.links[rowState] = rowLinks
            self.totals[rowState] = rowTotal
        
        