from bullet.Bullet import Bullet
from Map import Mapp
from Turret import Turret


class Tank:

    tank_size = 40

    def __init__(self, pos, map):
        self.pos = pos
        self.turret = Turret()  # Создаем дуло
        self.bullets = []
        self.map: Mapp = map

    def move(self, map: Mapp):

        self.pos.move()

        if (map.size_cell * map.size_x) - self.tank_size <= self.pos.x:
            self.pos.x = (map.size_cell * map.size_x) - self.tank_size
        if (map.size_cell * map.size_y) - self.tank_size <= self.pos.y:
            self.pos.y = (map.size_cell * map.size_y) - self.tank_size
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.x < 0:
            self.pos.x = 0

    def rotate(self, angular_speed):
        self.pos.rotate(angular_speed)

    def rotate_turret(self, angular_speed):
        """Поворот дуло."""
        self.turret.rotate(angular_speed)

    def spawn_bullet(self):
        """Создание новой пули на основе позиции дуло."""
        bullet = Bullet(self.pos.x, self.pos.y, self.turret.get_angle())
        self.bullets.append(bullet)
        print(f"Spawned bullet at {bullet.get_position()}")
