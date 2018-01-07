from __future__ import print_function
from time import sleep

import os
import numpy as np


class Game(object):
    def __init__(self, start_pos_snake, width, height, initial_direction):
        self.busy = True
        self.snake = [start_pos_snake, start_pos_snake - initial_direction, start_pos_snake - initial_direction - initial_direction]
        self.width = width
        self.height = height
        self.direction = initial_direction
        self.food_counters = []

    def stop(self):
        self.busy = False

    def tick(self):
        last_position = self.snake[len(self.snake) - 1]
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = self.snake[i - 1]

        self.snake[0] = self.snake[0] + self.direction

        if len(self.food_counters) != 0 and self.food_counters[0] == 0:
            self.snake.append(last_position)
            self.food_counters.remove(0)

        for i in range(len(self.food_counters)):
            self.food_counters[i] -= 1


def draw_field(width, height, objects):
    cls()
    line_horizontal = "+" + ("-" * width) + "+"
    print(line_horizontal)

    symbols = [[" " for j in range(width)] for i in range(height)]
    for x, y, s in objects:
        symbols[y][x] = s

    for i in range(height):
        print("|" + "".join(symbols[i]) + "|")

    print(line_horizontal)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


game = Game(np.array([2, 2]), 20, 10, np.array([1, 0]))

while game.busy:
    try:
        objects = [(game.snake[i][0], game.snake[i][1], "*" if i == 0 else "-") for i in range(len(game.snake))]
        draw_field(game.width, game.height, objects)
        sleep(0.5)
        game.tick()
    except KeyboardInterrupt:
        game.stop()



