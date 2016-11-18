from config import *
import json
import logging
import messages as m
import snakesock

class BaseSnake:
    def __init__(self, logging_level=logging.INFO):
        self.handlers = {
            m.GAME_ENDED : self.on_game_ended,
            m.TOURNAMENT_ENDED : self.on_tournament_ended,
            m.MAP_UPDATE : self.on_map_update,
            m.SNAKE_DEAD : self.on_snake_dead,
            m.GAME_STARTING : self.on_game_starting,
            m.PLAYER_REGISTERED : self.on_player_registered,
            m.INVALID_PLAYER_NAME : self.on_invalid_player_name,
            m.HEART_BEAT_RESPONSE : self.on_heart_beat_response,
            m.GAME_LINK_EVENT : self.on_game_link,
            m.GAME_RESULT_EVENT : self.on_game_result 
        }
        logging.basicConfig(format=FORMAT)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging_level)
        self.sock = snakesock.Snakesock()

    def log(self, log_level, msg):
        self.logger.log(log_level, msg)

    def connect(self):
        self.sock.connect(HOST, PORT, VENUE)

    def connected(self):
        return self.sock.connected()

    def register(self):
        self.sock.send(json.dumps(m.client_info()))
        self.sock.send(json.dumps(m.player_registration(SNAKE_NAME)))

    def get_message_handler(self, msg_type):
        try:
            return self.handlers[msg_type]
        except KeyError:
            return None

    def on_game_ended(self, _):
        self.logger.info("Game has ended")
        if VENUE == "training":
            self.sock.close()

    def on_map_update(self, msg):
        game_map = msg['map']
        move = self.get_next_move(game_map)
        self.logger.info("Snake is making move {} at worldtick: {}".format(move, game_map["worldTick"]))
        self.logger.debug("Responding to map udate")
        self.register_move(move, msg)

    def register_move(self, move, msg):
        self.sock.send(json.dumps(m.register_move(move, msg)))

    def on_tournament_ended(self, _):
        self.logger.info("Tournament has ended")
        return True

    def on_snake_dead(self, msg):
        death_reason = msg['deathReason']
        self.logger.info("Our snake has died, reason was: {}".format(death_reason))

    def on_game_starting(self, _):
        self.logger.info("Game is starting")

    def on_player_registered(self, msg):
        self.logger.info("Player was successfully registered")
        game_mode = msg['gameMode']
        if game_mode == "TRAINING":
            self.logger.debug("Requesting a game start")
            self.sock.send(json.dumps(m.start_game()))

    def on_invalid_player_name(self, _):
        self.logger.info("The player name is invalid, try another?")

    def on_heart_beat_response(self, _):
        pass

    def on_game_link(self, msg):
        self.logger.info("Watch game at: {}".format(msg['url']))

    def on_game_result(self, msg):
        player_ranks = msg['playerRanks']
        self.logger.info("Game result:")
        for number, player in enumerate(player_ranks):
            self.logger.info("{}. {:3d} pts   {} ({})".format(player["rank"], player["points"], player["playerName"], "alive" if player["alive"] else "dead"))

    def receive(self):
        msg = self.sock.recv()
        self.route_message(msg)

    def route_message(self, msg):
        self.logger.debug("Received message {}".format(msg))

        json_msg = json.loads(msg)
        msg_type = json_msg['type']

        self.logger.debug("Received message of type {}".format(msg_type))

        msg_handler = self.get_message_handler(msg_type)

        if msg_handler:
            msg_handler(json_msg)
        else:
            pass
