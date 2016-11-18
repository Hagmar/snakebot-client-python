#!/usr/bin/python3
import snake

def main():
    my_snake = snake.Snake()
    my_snake.connect()
    my_snake.register()

    while my_snake.connected():
        my_snake.receive()

if __name__ == '__main__':
    main()
