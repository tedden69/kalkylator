
_gameArea = None
GAMESIZE = 10

def initGameArea():
    global _gameArea

    _gameArea = [[' ' for _ in range(GAMESIZE)] for _ in range(GAMESIZE)]


def printWorm(worm):

    global _gameArea

    if _gameArea is None:
        initGameArea()

    pos = 0
    for nextElement in worm:
        charToPrint = 'o'
        if pos == 0:
            charToPrint = 'O'
        pos += 1

        if nextElement[0] < 0 or nextElement[0] > (GAMESIZE - 1) or \
            nextElement[1] < 0 or nextElement[1] > (GAMESIZE - 1):
            raise Exception("Your worm is out of bounds... Fix!")


        _gameArea[nextElement[0]][nextElement[1]] = charToPrint

    printableGameArea = ""
    for x in range(GAMESIZE):

        for y in range(GAMESIZE):
            printableGameArea += _gameArea[x][y]
        printableGameArea += "\n"

    print(printableGameArea)
            



if __name__ == "__main__":

    worm = [[2,2], [2,3], [2,4]]

    printWorm(worm)
