from proj.Map import Mapp
from proj.bullet.Bullet import Bullet
from proj.Pos import Pos

class BulletPool:

    speedBullets = 10


    def __init__(self, map: Mapp):
        self.map = map
        self.pullBullets = []

    def add_Bullet(self, tank):
        pos = Pos(tank.pos.x, tank.pos.y, self.speedBullets, tank.turret.angle, 0)
        bullet = Bullet(pos, tank)
        self.pullBullets.append(bullet)

    def update(self):
        for bullet in self.pullBullets:
            bullet.move()