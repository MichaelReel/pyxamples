from collections import namedtuple, deque

inputs = [
    'CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY',
    'NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS'
]

def rotateVect90((x, y), cwise = True):
    """
    rotate a vector of the form (x, y) where one value is zero and the other is +/-1
    by 90 degrees where cwise indicates clockwise if true, anticlockwise otherwise
    """
    return (-y if y != 0 else y, x) if cwise else (y, -x if x != 0 else x)

def wordSnake(words):
    # canvas is a deque of deques, so we can expand in any direction
    canvas = deque()
    canvas.append(deque(words[0][0]))
    fillChar = '-'

    def printCanvas():
        for line in canvas:
            print ''.join(line)

    def checkDir((x, y),(dx,dy), word):
        """
        start is a tuple in the form (x, y) and is the starting position for the 
        check. vect is a direction in the form (dx, dy) at 90 degs with scale 1
        and is the direction for the check.
        If we can travel across the canvas (or reach an edge) without colliding 
        with a word, the checkDir returns true.
        """
        pos = (x + dx, y + dy)
        while 0 <= pos[0] < len(canvas) and 0 <= pos[1] < len(canvas[y]):
            if canvas[y][x] != fillChar:
                return False
            pos = (pos[0] + dx, pos[1] + dy)
        return True

    def insertWord((x,y),(dx,dy), word):
        """
        start is a tuple in the form (x, y) and is the starting position for the 
        check. vect is a direction in the form (dx, dy) at 90 degs with scale 1
        and is the direction for the check.
        Insert the word across the canvas and expand the canvas where necessary
        Return the new "start" position for the next word
        """
        print x, y, dx, dy, word

        pos = (x,y)

        # Check for last char position overlapping the current bounds
        left  = 0 if dx >= 0 else  (-dx * (len(word) - 1)) - x
        up    = 0 if dy >= 0 else  (-dy * (len(word) - 1)) - y
        right = 0 if dx <= 0 else (( dx * (len(word) - 1)) + x) - (len(canvas[y]) - 1)
        down  = 0 if dy <= 0 else (( dy * (len(word) - 1)) + y) - (len(canvas) - 1)

        print left, up, right, down

        # expand the boundaries and update the pos, where applicable
        if left:
            for line in canvas:
                line.extendleft([fillChar] * left)
            pos = (pos[0] + left, pos[1])
        if up:
            width = len(canvas[y])
            for n in range(up):
                canvas.appendleft(deque([fillChar] * width))
            pos = (pos[0], pos[1] + up)
        if right:
            for line in canvas:
                line.extend([fillChar] * right)
        if down:
            width = len(canvas[y])
            for n in range(down):
                canvas.append(deque([fillChar] * width))

        # Insert the word and update the pos to the end point
        for c in word[1:]:
            pos = (pos[0] + dx, pos[1] + dy)
            canvas[pos[1]][pos[0]] = c

        printCanvas()
        return pos
                
            

    vect = (0,1)

    pos = insertWord(( 0, 0), ( 0,-1), "spoon")
    pos = insertWord(    pos, ( 1, 0), "spoon")
    pos = insertWord(    pos, ( 0, 1), "spoon")
    pos = insertWord(    pos, (-1, 0), "spoon")

    # for word in words:



# Just go right with every second word
wordSnake(inputs[0].split(" "))
# wordSnake(inputs[1].split(" "))