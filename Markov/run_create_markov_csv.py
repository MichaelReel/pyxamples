from markov import MarkovTable

inputFile = 'enable1.txt'
csvFileName = 'chains_1letter.csv'

with open(inputFile) as inf:
    print "Creating Markov Tables"
    markov = MarkovTable(input=inf, split = '1letter')
    print "Tables generated"

with open(csvFileName, "wb") as csvFile:
    print "Saving csv"
    markov.writeCSV(csvFile)
    print "CSV saved"
