import pygame as pg
import random

# Resolution of the screen.
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

# Colours that was used in designing program.
BLACK = (0, 0, 0)
DARKSLATEBLUE = (72, 61, 139, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MIGHTYBLUE = (79, 153, 209)
GRAY = (204, 204, 204)
LIGHTGREEN = (144, 238, 144, 255)
ROYALBLUE1 = (72, 118, 255, 255)

# Images that was used in program.
ttt = pg.image.load('img\pic.png')
bot = pg.image.load('img\hi.png')
cross = pg.image.load('img\cross.png')
circle = pg.image.load('img\circle.png')

# Fun facts
facts = ['British name of Tic-Tac-Toe is Noughts and Croses.', 'Game can be tracked back to ancient Egypt.', 'Tic-Tac-Toe became one of first known video games.',
         'Avarage playtime is ~1 minute.', 'There are Championships in Tic-Tac-Toe.', 'In Japan 5x5 Tic-Tac-Toe was named Gomoku.']
randomFact = facts[random.randint(0, 5)]

pg.init()

# Display and name of program.
displayWindow = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Tic-Tac-Toe Project')


class MenuDisplay:
    # 'MenuDisplay' class represent the initial screen when the game is launched for the first time and after gameplay.

    # Variable 'boardSize' is the default board size.
    # Variable 'defaultWin' is the default winning condition
    boardSize = 3
    defaultWin = 3

    def boardUp(self) -> None:
        # Function to increment size of the board (max 10x10).

        if self.boardSize < 10:
            self.boardSize += 1
            self.defaultWin += 1

    def winUp(self) -> None:
        # Function to increment winning condition (max is the size of row/column in board (10)).

        if self.defaultWin < 10 and self.defaultWin < self.boardSize:
            self.defaultWin += 1

    def boardDown(self) -> None:
        # If the board size in decrementing this function also decrement winning condition,
        # because it cannot be higher that size of the board.

        if self.boardSize > 3:
            self.boardSize += -1
            if self.defaultWin > self.boardSize:
                self.defaultWin += -1

    def winDown(self) -> None:
        # Function to decrement win condition (min is 3).

        if self.defaultWin > 3:
            self.defaultWin += -1

    def notification(self, size: int, message: str, colour: tuple, position: tuple) -> None:
        # Display message on desired size/position/colour.
        # Parameter 'size' represent size of text.
        # Parameter 'message' is a string displayed on the screen.
        # Parameter 'colour' sets colour of the message (defined at the beginning of the module).
        # Parameter 'position' sets displayed text on x and y coordinates.

        text = pg.font.Font(None, size)
        textSurface = text.render(message, True, colour)
        textRectangle = textSurface.get_rect()
        textRectangle.center = position
        displayWindow.blit(textSurface, textRectangle)

    def buttons(self, position: tuple, width: int, height: int, rectangleColour: tuple, message: str,
                        messageColour: tuple, action=None) -> None:
        # Function display buttons and calls functions after clicking on them.

        # Parameter 'action' is the function called after clicking.
        # Parameter 'height'/'width' is size of the buttons.
        # Parameter 'message' text displayed on the buttons.
        # Parameter 'messageColour' is the colour of displayed text.
        # Parameter 'rectangleColour' is the colour of displayed buttons.
        # Parameter 'position' is the position of buttons by x and y coordinates.

        mouseCursor = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()

        if (position[0] - width / 2) < mouseCursor[0] < (position[0] + width / 2) and \
                position[1] < mouseCursor[1] < (position[1] + height):
            if mouseClick[0] == 1 and action is not None:
                pg.time.delay(200)
                if action():
                    # This function is 'TRUE' only when game is finished,
                    # to protect START button from printing too fast.
                    return
        pg.draw.rect(displayWindow, rectangleColour, ((position[0] - (width / 2), position[1]), (width, height)))
        self.notification(int(height / 2), message, messageColour, (position[0], position[1] + height / 2))

    def printElements(self, runMain):
        # Display all elements of starting screen.

        # Function 'runMain' runs the game.

        displayWindow.fill(WHITE)
        self.notification(120, 'Tic-Tac-Toe', RED, (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.06))
        self.notification(60, 'Versus AI gameplay! ', RED, (WINDOW_WIDTH * 0.51, WINDOW_HEIGHT * 0.135))
        self.notification(60, 'Fun fact:', MIGHTYBLUE, (WINDOW_WIDTH * 0.50, WINDOW_HEIGHT * 0.24))
        self.notification(40, randomFact, MIGHTYBLUE, (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.29))
        displayWindow.blit(ttt, (WINDOW_WIDTH * 0.59, WINDOW_HEIGHT * 0.33))
        displayWindow.blit(bot, (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT * 0.31))
        self.notification(40, 'Choose size of board:', MIGHTYBLUE, (WINDOW_WIDTH * 0.265, WINDOW_HEIGHT * 0.675))
        self.buttons((WINDOW_WIDTH * 0.125, WINDOW_HEIGHT * 0.7), 50, 50, GRAY, "-", BLACK, self.boardDown)
        self.buttons((WINDOW_WIDTH * 0.408, WINDOW_HEIGHT * 0.7), 50, 50, GRAY, "+", BLACK, self.boardUp)
        self.buttons((WINDOW_WIDTH * 0.266, WINDOW_HEIGHT * 0.7), 150, 50, DARKSLATEBLUE, str(self.boardSize), LIGHTGREEN)
        self.notification(40, 'Choose amount to win: ', MIGHTYBLUE, (WINDOW_WIDTH * 0.29, WINDOW_HEIGHT * 0.825))
        self.buttons((WINDOW_WIDTH * 0.125, WINDOW_HEIGHT * 0.85), 50, 50, GRAY, "-", BLACK, self.winDown)
        self.buttons((WINDOW_WIDTH * 0.408, WINDOW_HEIGHT * 0.85), 50, 50, GRAY, "+", BLACK, self.winUp)
        self.buttons((WINDOW_WIDTH * 0.266, WINDOW_HEIGHT * 0.85), 150, 50, DARKSLATEBLUE, str(self.defaultWin), LIGHTGREEN)
        self.buttons((WINDOW_WIDTH * 0.77, WINDOW_HEIGHT * 0.7), 200, 150, DARKSLATEBLUE, 'START', LIGHTGREEN, runMain)


class GameDisplay:
    # 'GameDisplay' class displays game screen, store size informations and current state of the board.

    def __init__(self, size, winCondition):
        self.size = size
        self.winCondition = winCondition
        self.gridSize = WINDOW_WIDTH / (1.1 * self.size + 0.1) # Size of grid, where tags are placed.
        self.spaceSize = 0.1 * self.gridSize # Space between grid.
        self.tags = [[None for x in range(self.size)] for y in range(self.size)] # Current size of board.
        self.cross = self.resizeElements(cross, True) # Resizing 'cross' image by size of the board.
        self.circle = self.resizeElements(circle, False)  # Resizing 'circle' image by size of the board.

    def resizeElements(self, image: pg.SurfaceType, whichTag: bool) -> pg.SurfaceType:
        # Resizing elements (cross/circle image).
        # Returns resized image.

        # Parameter 'image' represents image (it is pygame class).
        # Parameter 'size' is the size of board.
        # Parameter 'whichTag' decides which image should be displayed.

        if whichTag:
            x = 1.22
            y = 1.22
        else:
            x = 1.65
            y = 1.65

        imageRectangle = image.get_rect()
        image = pg.transform.scale(image, (int(x / self.size * imageRectangle.width), int(y / self.size * imageRectangle.height)))
        return image

    def grid(self) -> None:
        # Function to print game grid, where X and O will be placed.

        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                pg.draw.rect(displayWindow, GRAY, [j*self.spaceSize+(j-1)*self.gridSize,
                                                   i*self.spaceSize+(i-1)*self.gridSize, self.gridSize, self.gridSize])

    def elements(self) -> None:
        # Function to print X and O on the game board.
        # Actual state of game.

        for i in range(1, self.size + 1):
            x = i * self.spaceSize + (i - 1) * self.gridSize
            for j in range(1, self.size + 1):
                y = j * self.spaceSize + (j - 1) * self.gridSize
                if self.tags[i-1][j-1] == 'x':
                    displayWindow.blit(self.cross, (x, y))
                elif self.tags[i-1][j-1] == 'o':
                    displayWindow.blit(self.circle, (x, y))

    def components(self) -> None:
        # Function to display all components of game screen.

        displayWindow.fill(WHITE)
        self.grid()
        self.elements()