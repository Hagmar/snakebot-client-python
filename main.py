#!/usr/bin/python3
import snakesock
import messages
import json
import snake

def route_message(message):
    json_msg = json.loads(message)
    msg_type = json_msg['type']
    msg_handler = snake.get_message_handler(msg_type)
    msg_handler()

def main():
    my_snake = snake.Snake()

    sock = snakesock.Snakesock()
    sock.connect("snake.cygni.se", 80)

    sock.send(json.dumps(messages.client_info()))
    sock.send(json.dumps(messages.player_registration(my_snake.name)))

    while True:
        message = sock.recv()
        if not message:
            break
        route_message(message)


if __name__ == '__main__':
    main()
