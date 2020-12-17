class Bot():
    def __init__ (self, direction, startX, startY):
        self.direction = None
        self.startX = None
        self.startY = None
class Maze():
    def __init__ (self, wall, open, end):
        self.wall = '#'
        self.open = '-'
        self.end = 'e'
    def createRandom(self):
        length = random.random()
