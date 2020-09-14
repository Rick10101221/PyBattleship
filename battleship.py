# battleship
from random import randint

class board:
    def __init__(self):
        n=5
        self.gameBoard = []
        for i in range(n):
            currRow = []
            for j in range(n):
                currRow.append('O')
            self.gameBoard.append(currRow)

        self.shipX, self.shipY = randint(0,n-1), randint(0,n-1)
        self.maxTries = (n**2) // 4
        self.win = False
    
    def markWrong(self, x, y):
        self.gameBoard[x][y] = 'X'

    def playerGuess(self):
        x = input('Guess Row: ')
        y = input('Guess Column: ')
        self.checkGuess(x, y)

    def checkGuess(self, x , y):
        validGuess = False
        print()
        n = len(self.gameBoard)
        if not(x.isdigit() and y.isdigit()):
            print('Uh Oh Stinky, try again')
            self.maxTries += 1
        elif (int(x) <= 0 or n < int(x)) or (int(y) <= 0 or n < int(y)):
            print('Make a guess thats on the board, you fool')
            self.maxTries += 1
        elif self.gameBoard[int(x) - 1][int(y) - 1] == 'X':
            print('Sounds familiar, you\'ve guessed that one already')
            self.maxTries += 1
        elif self.shipX == int(x) - 1 and self.shipY == int(y) - 1:
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
        if not(boardObj.win)
            print()
        if boardObj.win:
            print('Congrats, you Won!')
            exit()
        elif boardObj.maxTries == 0:
            print('You are a disgrace to your family')
            exit()

startGame()