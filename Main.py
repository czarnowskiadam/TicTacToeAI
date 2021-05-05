from Movement import *

class Main:
    # 'Main' class runs all the functions like screen and operate practicality.

    def __init__(self):
        self.operations = None
        self.entryDisplay = MenuDisplay()

    def finalScreen(self, message: str) -> None:
        # Final screen (win, lose, draw).
        # To continue player have to click anywhere on the screen.
        # variable 'message' display proper message.

        finalScreen = True
        while finalScreen:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    finalScreen = False
                    pg.time.delay(200)

            self.entryDisplay.notification(155, message, ROYALBLUE1, (350, 325))
            self.entryDisplay.notification(80, 'Click to continue...', ROYALBLUE1, (350, 400))

            pg.display.update()

    def gameScreen(self) -> int:
        # Run and display game screen.
        # Prints board, grid and notifications.
        # Make decision which turn is it and after each turn checks for winner or draw.

        run = True
        self.operations = Movement(self.entryDisplay.boardSize, self.entryDisplay.defaultWin)
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False

            self.operations.components()
            if self.operations.whilePlayer:
                self.operations.playerTurn()
            else:
                self.entryDisplay.notification(90, 'LOADING...', MIGHTYBLUE, (350, 350))
                pg.display.update()
                self.operations.aiTurn()
                self.operations.whilePlayer = True
            pg.display.update()
            self.operations.components()

            if self.operations.checkWin('o'):
                run = False
                self.finalScreen('DEFEAT')
            elif self.operations.checkWin('x'):
                run = False
                self.finalScreen('VICTORY')
            elif self.operations.fullBoard():
                run = False
                self.finalScreen('DRAW')
        return 1

    def firstScreen(self) -> None:
        # Function that run first screen after launching game.
        # In this function it is possibility to change board size and winning condition using buttons.
        # Start button included.

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        quit()
            self.entryDisplay.printElements(self.gameScreen)
            pg.display.update()

if __name__ == '__main__':
    game = Main()
    game.firstScreen()