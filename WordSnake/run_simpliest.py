inputs = [
    'CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY',
    'NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS'
]

def wordSnake(words):
    def printDown(word, pre):
        for i in word[1 if pre else 0:-1:]:
            print ' ' * pre, i

    def printLeft(word, pre):
        print ' ' * pre, word

    pre = 0
    for i, word in enumerate(words):
        if i % 2:
            printLeft(word, pre)
            pre += len(word) - 1
        else:
            printDown(word, pre)

# Just go right with every second word
wordSnake(inputs[0].split(" "))
wordSnake(inputs[1].split(" "))