from Display import *

INF = 1e10  # represents INF


class AI(GameDisplay):
    # 'AI' class implements algorithm that checks current state of the board.
    # Representation the way of "thinking" of AI.

    def checkColumns(self, win: list) -> bool:
        # Function checks all columns for winning composition.
        # Parameter 'win' is a list that represent winning composition. If the winning conditions equal to 4,
        # 'win' is equal to ['x', 'x', 'x', 'x']. The same with AI, but instead X is O.
        # Returns 'True' if composition was found in column.

        for row in range(self.size):
            column = [self.tags[x][row] for x in range(self.size)]
            for j in range(len(column) - len(win) + 1):
                if win == column[j:j+self.winCondition]:
                    return True

    def checkRows(self, win: list) -> bool:
        # Function is quite the same as in 'checkColumns', but instead columns it search for rows.

        for row in self.tags:
            for j in range(len(row) - len(win) + 1):
                if win == row[j:j+self.winCondition]:
                    return True

    def checkDiagonals(self, win: list) -> bool:
        # Function is quite the same as in 'checkColumns', but instead columns it search for diagonals.
        # Below are ways of checking diagonals.

        for i in range(self.size - self.winCondition + 1):
            diagonal = []
            x = i
            y = 0
            for j in range(self.size - i):
                diagonal.append(self.tags[x][y])
                x += 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + self.winCondition]:
                    return True

            diagonal = []
            x = 0
            y = i
            for j in range(self.size - i):
                diagonal.append(self.tags[x][y])
                x += 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + self.winCondition]:
                    return True

            diagonal = []
            x = self.size - 1 - i
            y = 0
            for j in range(self.size - i):
                diagonal.append(self.tags[x][y])
                x -= 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + self.winCondition]:
                    return True

            diagonal = []
            x = self.size - 1
            y = 0 + i
            for j in range(self.size - i):
                diagonal.append(self.tags[x][y])
                x -= 1
                y += 1
            for j in range(len(diagonal) - len(win) + 1):
                if win == diagonal[j:j + self.winCondition]:
                    return True

    def checkWin(self, tag: str) -> bool:
        # Function checks if the winning sequence is achieved.
        # Parameter 'tag' is a cross/circle that must be in 'winningLine'.
        # Returns 'True' if the sequence was found.

        winningLine = [tag]*self.winCondition
        return self.checkRows(winningLine) or self.checkColumns(winningLine) or self.checkDiagonals(winningLine)

    def fullBoard(self) -> bool:
        # Function checks if the board is full.
        # Return is a bool that decide about filled board.

        counter = 0
        for column in self.tags:
            if None in column:
                counter += 1
        return counter == 0

    def checkMoves(self) -> list:
        # Function scan board for empty spaces.
        # If there some, they are added to the new list.
        # Returns available spaces.

        availableMoves = []
        for x in range(self.size):
            for y in range(self.size):
                if self.tags[x][y] is None:
                    availableMoves.append((x, y))
        return availableMoves

    def aiMove(self) -> None:
        # Function realize AI move.
        # Also calls the 'mmAlgorithm'.

        # Variable 'maximiseValue' is the best value for maximising player.
        # AI is maximising player.
        maximiseValue = -INF
        getableMoves = self.checkMoves()

        # Variable 'depth' decide about deep recursion of the algorithm.
        # In this program I have decided to point 1.45.
        # I think the 1.45 gives best unity between execution and precision of moves.
        depth = int(1.4*self.size - self.winCondition)
        bestMove = None
        for move in getableMoves:
            self.tags[move[0]][move[1]] = 'o'
            moveValue = self.mmAlgorithm(depth, -INF, INF, False)
            self.tags[move[0]][move[1]] = None
            if moveValue > maximiseValue:
                maximiseValue = moveValue
                bestMove = move

        self.tags[bestMove[0]][bestMove[1]] = 'o'

    def mmAlgorithm(self, depth: int, first: float, second: float, maxminTurn: bool) -> float:
        # Algorithm include pruning that avoid overfitting.
        # Parameter 'depth' decide about the depth.
        # Parameter 'first'/'second' is a factor of puring.
        # Parameter 'maxminTurn' is a bool that decide which player's turn is.
        # Returns value (0, 1, -10, 10) when the function is called recursively down the heap.
        # or
        # Returns best value when function is called recursively up the heap.

        if self.checkWin('x' if maxminTurn is True else 'o'):
            return -10 if maxminTurn else 10
        if self.fullBoard():
            return 1
        if depth == 0:
            return 0

        getableMoves = self.checkMoves()

        if maxminTurn:
            maxEvaluation = -INF
            for move in getableMoves:
                self.tags[move[0]][move[1]] = 'o'
                evaluation = self.mmAlgorithm(depth - 1, first, second, False)
                self.tags[move[0]][move[1]] = None
                maxEvaluation = max(maxEvaluation, evaluation)
                first = max(first, evaluation)
                if second <= first:
                    break
            return maxEvaluation

        else:
            minEvaluation = INF
            for move in getableMoves:
                self.tags[move[0]][move[1]] = 'x'
                evaluation = self.mmAlgorithm(depth - 1, first, second, True)
                self.tags[move[0]][move[1]] = None
                minEvaluation = min(minEvaluation, evaluation)
                first = min(second, evaluation)
                if second <= first:
                    break
            return minEvaluation