import messages

class Snake:
    name = "The Python"
    handlers = {
        'GAME_ENDED' : on_game_ended,
        'TOURNAMENT_ENDED' : on_tournament_ended,
        'MAP_UPDATE' : on_map_update,
        'SNAKE_DEAD' : on_snake_dead,
        'GAME_STARTING' : on_game_starting,
        'PLAYER_REGISTERED' : on_player_registered,
        'INVALID_PLAYER_NAME' : on_invalid_player_name,
        'HEART_BEAT_RESPONSE' : on_heart_beat_response,
        'GAME_LINK_EVENT' : on_game_link,
        'GAME_RESULT_EVENT' : on_game_result 
    }

    def get_message_handler(self, msg_type):
        try:
            return self.handlers[msg_type]
        except KeyError:
            return None
