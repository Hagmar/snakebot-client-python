import json
from sys import version_info

# Inbound
GAME_ENDED = "se.cygni.snake.api.event.GameEndedEvent"
TOURNAMENT_ENDED = "se.cygni.snake.api.event.TournamentEndedEvent"
MAP_UPDATE = "se.cygni.snake.api.event.MapUpdateEvent"
SNAKE_DEAD = "se.cygni.snake.api.event.SnakeDeadEvent"
GAME_STARTING = "se.cygni.snake.api.event.GameStartingEvent"
PLAYER_REGISTERED = "se.cygni.snake.api.response.PlayerRegistered"
INVALID_PLAYER_NAME = "se.cygni.snake.api.exception.InvalidPlayerName"
HEART_BEAT_RESPONSE = "se.cygni.snake.api.response.HeartBeatResponse"
GAME_LINK_EVENT = "se.cygni.snake.api.event.GameLinkEvent"
GAME_RESULT_EVENT = "se.cygni.snake.api.event.GameResultEvent"

# Outbound
REGISTER_PLAYER_MESSAGE_TYPE = "se.cygni.snake.api.request.RegisterPlayer"
START_GAME = "se.cygni.snake.api.request.StartGame"
REGISTER_MOVE = "se.cygni.snake.api.request.RegisterMove"
HEART_BEAT_REQUEST = "se.cygni.snake.api.request.HeartBeatRequest"
CLIENT_INFO = "se.cygni.snake.api.request.ClientInfo"


def start_game():
    start_game_msg = { "type" : START_GAME }
    return start_game_msg

def client_info():
    version = "{0[0]}.{0[1]}.{0[2]}".format(version_info[:3])
    client_info_msg = {
        "type" : CLIENT_INFO,
        "language" : "Python",
        "languageVersion" : version,
        "operatingSystem" : "",
        "operatingSystemVersion" : "",
        "clientVersion" : "0.1"
    }

    return client_info_msg

def default_game_settings():
    game_settings = {
        "maxNoofPlayers" : 5,
        "startSnakeLenth" : 1,
        "timeInMsPerTick" : 250,
        "obstaclesEnabled" : True,
        "foodEnabled" : True,
        "headToTailConsumes" : True,
        "tailConsumeGrows" : False,
        "addFoodLikelihood" : 15,
        "removeFoodLikelihood" : 5,
        "spontaneousGrowthEveryNWorldTick" : 3,
        "trainingGame" : False,
        "pointsPerLength" : 1,
        "pointsPerFood" : 2,
        "pointsPerCausedDeath" : 5,
        "pointsPerNibble" : 10,
        "noofRoundsTailProtectedAfterNibble" : 3
    }

    return game_settings

def player_registration(snake_name):
    player_registration_msg = {
        "type" : REGISTER_PLAYER_MESSAGE_TYPE,
        "playerName" : snake_name,
        "gameSettings" : default_game_settings()
    }

    return player_registration_msg

def register_move(next_move, incoming_json):
    register_move_msg = {
        "type" : REGISTER_MOVE,
        "direction" : next_move,
        "gameTick" : incoming_json["gameTick"],
        "receivingPlayerId" : incoming_json["receivingPlayerId"],
        "gameId" : incoming_json["gameId"]
    }

    return register_move_msg;
