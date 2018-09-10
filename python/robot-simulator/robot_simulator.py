# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

    
class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.bearing = bearing

    @property
    def coordinates(self):
        return (self.x,self.y)

    def advance(self):
        if self.bearing == EAST:
            self.x += 1
        elif self.bearing == NORTH:
            self.y +=1
        elif self.bearing == WEST:
            self.x -= 1
        else: #south
            self.y -=1

    def turn_right(self):
        self.bearing = (self.bearing -1) %4
    def turn_left(self):
        self.bearing = (self.bearing +1) % 4

    def simulate(self, instructions):
        for x in instructions:
            if x == 'A': self.advance()
            elif x == 'R': self.turn_right()
            elif x ==  'L' : self.turn_left()
