from basesnake import BaseSnake
from config import LOGGING_LEVEL

class Snake(BaseSnake):
    def get_next_move(self, game_map):
        move = "DOWN"
        return move
