from AI import *
from Player import *


class Movement(AI, Player):
    # 'Movement' class inherits from AI, Player and GameDisplay.
    
    def __init__(self, size, winCondition):
        super().__init__(size, winCondition)

    def playerTurn(self) -> None:
        # From 'Player' module calls method that is responsible for player move.
        self.playerMove()

    def aiTurn(self) -> None:
        # From 'AI' module calls method that is responsible for AI move.
        # Change turn from AI to Player.
        self.aiMove()
        self.whilePlayer = True