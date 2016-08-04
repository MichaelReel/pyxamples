from markov import MarkovTable

inputFile = 'enable1.txt'
jsonFileName = 'chains_consonants.json'

with open(inputFile) as inf:
    print "Creating Markov Tables"
    markov = MarkovTable(input=inf, split = 'consonants')
    print "Tables generated"

with open(jsonFileName, "wb") as jsonFile:
    print "Saving JSON"
    markov.writeJSON(jsonFile)
    print "JSON saved"