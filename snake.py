from basesnake import BaseSnake
from config import LOGGING_LEVEL

class Snake(BaseSnake):
    def __init__(self, logging_level=LOGGING_LEVEL):
        super().__init__(logging_level)

    def get_next_move(self, game_map):
        move = "DOWN"
        return move
