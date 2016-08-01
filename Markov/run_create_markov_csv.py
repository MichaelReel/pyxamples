from markov import MarkovTable

inputFile = 'enable1.txt'
csvFileName = 'enable1_chains.csv'

with open(inputFile) as inf:
    print "Creating Markov Tables"
    markov = MarkovTable(input=inf)
    print "Tables generated"

with open(csvFileName, "wb") as csvFile:
    print "Saving csv"
    markov.writeCSV(csvFile)
    print "CSV saved"
