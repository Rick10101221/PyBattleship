# battleship
# Authors: Rylee Weaver, Rickesh Khilnani

from random import randint
from random import choice

class board:
    def __init__(self):
        n = input('Enter board size: ')
        while (not(n.isdigit()) or int(n) < 10):
            if (not(n.isdigit())):
                n = input('Bad input. Try again: ')
            else:
                n = input('Please select a larger board size: ')
                if (n.isdigit() and int(n) > 10):
                    break
        n = int(n)
        
        self.gameBoard = []
        for _ in range(n):
            currRow = []
            for _ in range(n):
                currRow.append('O')
            self.gameBoard.append(currRow)

        self.spawnShip()
        chanceForFirstHitShip = 0.9
        self.maxTries = round(n**2 * chanceForFirstHitShip)
        self.win = False

    def spawnShip(self):
        self.size = round(len(self.gameBoard) * (randint(2,5) / 10))
        shipRow, shipCol = randint(0, len(self.gameBoard) - 1), randint(0, len(self.gameBoard) - 1)
        self.shipCoordinates = {(shipRow, shipCol)}
        possibleDirections = {0,1,2,3}
        cardinalDirection = choice(tuple(possibleDirections))
        while(True):
            if (cardinalDirection == 0):
                if shipCol + self.size - 1 > len(self.gameBoard):
                    possibleDirections.discard(0)
                else:
                    for i in range(self.size - 1):
                        self.shipCoordinates.add((shipRow, shipCol + i + 1))
                    break
            elif (cardinalDirection == 1):
                if shipRow - self.size + 1 <= 0:
                    possibleDirections.discard(1)
                else:
                    for i in range(self.size - 1):
                        self.shipCoordinates.add((shipRow - i - 1, shipCol))
                    break
            elif (cardinalDirection == 2):
                if shipCol - self.size + 1 <= 0:
                    possibleDirections.discard(2)
                else:
                    for i in range(self.size - 1):
                        self.shipCoordinates.add((shipRow, shipCol - i - 1))
                    break
            else:
                if shipRow + self.size - 1 > len(self.gameBoard):
                    possibleDirections.discard(3)
                else:
                    for i in range(self.size - 1):
                        self.shipCoordinates.add((shipRow + i + 1, shipCol))
                    break
            cardinalDirection = choice(tuple(possibleDirections))
    
    def markWrong(self, x, y):
        self.gameBoard[x][y] = 'X'

    def markHit(self, x, y):
        self.gameBoard[x][y] = 'H'

    def playerGuess(self):
        x = input('Guess Row: ')
        y = input('Guess Column: ')
        self.checkGuess(x, y)

    def checkGuess(self, x, y):
        validGuess = False
        print()
        n = len(self.gameBoard)
        if not(x.isdigit() and y.isdigit()):
            print('Uh Oh Stinky, try again')
            self.maxTries += 1
        elif (int(x) <= 0 or n < int(x)) or (int(y) <= 0 or n < int(y)):
            print('Make a guess thats on the board, you fool')
            self.maxTries += 1
        elif self.gameBoard[int(x) - 1][int(y) - 1] == 'X' or\
             self.gameBoard[int(x) - 1][int(y) - 1] == 'H':
            print('Sounds familiar, you\'ve guessed that one already')
            self.maxTries += 1
        elif (int(x) - 1, int(y) - 1) in self.shipCoordinates:
            if self.size == len(self.shipCoordinates) and self.maxTries > self.size + 1:
                self.maxTries = self.size + 1
                for _ in range(4):
                    print('CAUTION TRIES HAVE BEEN REDUCED')
                print()
            print('Good job you hit something')
            self.markHit(int(x) - 1, int(y) - 1)
            validGuess = True
            self.shipCoordinates.discard((int(x) - 1, int(y) - 1))
            if (len(self.shipCoordinates) == 0):
                self.win = True
        else:
            print('Oof, you missed')
            self.markWrong(int(x) - 1, int(y) - 1)
            validGuess = True

        if validGuess == True:
            self.displayBoard()
        self.maxTries -= 1

    def displayBoard(self):
        print()
        n = len(self.gameBoard)
        for i in range(n):
            for j in range(n):
                print(self.gameBoard[i][j], end = ' ')
            print()
        print()

def startGame():
    boardObj = board()
    print(f'You have {boardObj.maxTries} tries remaining.' )
    while boardObj.win != True or boardObj.maxTries != 0:
        boardObj.playerGuess()
        if boardObj.maxTries != 1 and not(boardObj.win):
            print(f'You have {boardObj.maxTries} tries remaining.')
        elif not(boardObj.win):
            print(f'You have {boardObj.maxTries} try remaining.')
        if not(boardObj.win):
            print()
        if boardObj.win:
            print('Congrats, you Won!')
            exit()
        elif boardObj.maxTries == 0:
            print('You are a disgrace to your family')
            exit()

startGame()