from random import Random
import csv

class MarkovTable(object):
    
    def __init__(self, input=None, csvFile=None):
        self.links = {}
        self.totals = {}
        self.headers = set()
        if csvFile:
            self.readCSV(csvFile)
        if input:
            self.readInputStream(input)

    def readInputStream(self, input):
        for line in input.readlines():
            line = line.strip()
            self.insertWord(line)

    def insertWord(self, word):
        # Start and end with a space
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
        # Use space to find a starting letter:
        word = self.getRandomLinkedLetter(' ', rand)
        while word[-1] != ' ':
            word += self.getRandomLinkedLetter(word[-1], rand)
        return word
        
    def getRandomLinkedLetter(self, letter, rand):
        pos = rand.randint(0, self.totals[letter])
        for nextLetter in self.links[letter].keys():
            pos -= self.links[letter][nextLetter]
            if pos < 0:
                return nextLetter

    def writeCSV(self, file):
        writer = csv.writer(file)
        headers = sorted(self.headers)
        writer.writerow([''] + headers)
        for key in self.links.keys():
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
        
        