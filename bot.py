from Pos import Pos
from Tank import Tank

class Bot():
    def __init__(self, tank, map):
        self.tank = tank
        self.map = map

    def update(self):
        self.tank.move(self.map)