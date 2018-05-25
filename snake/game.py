import random
import curses

from snake import Snake
from food import Food
from board import Board


class Game(object):

    def __init__(self):
        self.board = Board()
        self.snake = Snake(self.board.width/4, self.board.height/2)
        self.food = Food(self.board.height/2, self.board.width/2)
        self.board.put_character(self.food.position[0], self.food.position[1], self.food.symbol)
        self.status = True


    def run(self):
        key = curses.KEY_RIGHT
        while self.status:
            next_key = self.board.window.getch()
            key = key if next_key == -1 else next_key
            self._is_exit()
            self.snake.insert_head(key)
            self._new_food()


    def _is_exit(self):
        if self.snake.body[0][0] in [0, self.board.height] or \
           self.snake.body[0][1]  in [0, self.board.width] or \
           self.snake.body[0] in self.snake.body[1:]:
            curses.endwin()
            quit()


    def _new_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = None
            while self.food.position is None:
                nf = [
                    random.randint(1, self.board.height - 1),
                    random.randint(1, self.board.width - 1)
                ]
                self.food.position = nf if nf not in self.snake.body else None
            self.board.put_character(self.food.position[0], self.food.position[1], self.food.symbol)
        else:
            tail = self.snake.body.pop()
            self.board.put_character(tail[0], tail[1], ' ')
        self.board.put_character(self.snake.body[0][0], self.snake.body[0][1], curses.ACS_CKBOARD)
