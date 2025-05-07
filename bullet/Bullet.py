import Pos
from Tank import Tank


class Bullet:
    def __init__(self, pos, tank: Tank):
        self.pos = pos
        self.tank = tank

    def move(self):
        """Перемещение пули в направлении угла."""
        self.pos.move()

    def get_position(self):
        """Получить текущие координаты пули."""
        return (self.x, self.y)

    def __str__(self):
        """Строковое представление объекта Bullet."""
        return f"Bullet(x={self.x}, y={self.y}, angle={self.angle})"