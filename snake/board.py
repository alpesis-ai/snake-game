import curses


class Board(object):

    def __init__(self):
        self.screen = curses.initscr()
        curses.curs_set(0)

        self.height, self.width = self.screen.getmaxyx()
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.keypad(1)
        self.window.timeout(100)

    def put_character(self, x, y, character):
        self.window.addch(x, y, character)
