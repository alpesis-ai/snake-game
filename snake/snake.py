import curses


class Snake(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.body = [
            [self.y, self.x],
            [self.y, self.x - 1],
            [self.y, self.x - 2]
        ]


    def insert_head(self, key):
        new_head = [self.body[0][0], self.body[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
             new_head[1] += 1
        return self.body.insert(0, new_head)
