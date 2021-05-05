from Display import *


class Player(GameDisplay):
    # Class 'Player' is representation of human player.

    # Decides of player turn.
    whilePlayer = True

    def playerMove(self) -> None:
        # Function checks localisation of the mouse cursor.
        # If cursor is inside grid it displays X, after clicking on grid the X is added.

        mouseCursor = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()

        for i in range(1, self.size + 1):
            x = i * self.spaceSize + (i - 1) * self.gridSize
            for j in range(1, self.size + 1):
                y = j * self.spaceSize + (j - 1) * self.gridSize
                if x < mouseCursor[0] < x + self.gridSize and y < mouseCursor[1] < y + self.gridSize and self.tags[i-1][j-1] is None:
                    displayWindow.blit(self.cross, (x, y))

                    if mouseClick[0] == 1:
                        self.tags[i-1][j-1] = 'x'
                        self.whilePlayer = False