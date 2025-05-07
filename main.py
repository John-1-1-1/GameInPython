import math



import pygame

from proj.Map import Mapp
from proj.bot import Bot
from proj.Pos import Pos
from proj.Tank import Tank


class Map:
    def __init__(self, map):

        self.map: Mapp = map
        self.color = (200, 200, 200)  # Цвет линий сетки

    def draw(self, surface):
        # Отрисовка вертикальных линий
        for x in range(0, self.map.size_x * self.map.size_cell, self.map.size_cell):
            pygame.draw.line(surface, self.color, (x, 0), (x, self.map.size_y * self.map.size_cell))

        # Отрисовка горизонтальных линий
        for y in range(0,  self.map.size_y * self.map.size_cell, self.map.size_cell):
            pygame.draw.line(surface, self.color, (0, y), (self.map.size_x * self.map.size_cell, y))

    def draw_tank(self, surface, bot):
        """Отрисовка танка на поверхности."""
        rect_x = bot.tank.pos.x
        rect_y = bot.tank.pos.y

        # Рисуем квадрат
        pygame.draw.rect(surface, (0, 255, 0), (rect_x, rect_y, 40, 40))

        center_x = rect_x + 20  # 40 / 2
        center_y = rect_y + 20  # 40 / 2
        
        # Вычисляем координаты конца дуло
        barrel_length = 30  # Длина дуло
        end_x = center_x + barrel_length * math.cos(math.radians(bot.tank.turret.angle))
        end_y = center_y + barrel_length * math.sin(math.radians(bot.tank.turret.angle))
        
        # Рисуем дуло танка
        pygame.draw.line(surface, (255, 0, 0), (center_x, center_y), (end_x, end_y), 5)

# Пример использования
pygame.init()

map = Mapp(20, 20, 50)


screen = pygame.display.set_mode((map.size_x * map.size_cell, map.size_y * map.size_cell))

map_grid = Map(  map)





start_pos = Pos(x=0, y=0, speed=5, angle=90, angular_speed=15)
bot = Bot(Tank(start_pos, map), map)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Очистка экрана
    map_grid.draw(screen)    # Отрисовка сетки

    bot.update()
    #time.sleep(1)
    map_grid.draw_tank(screen, bot)

    pygame.display.flip()  # Обновление экрана

pygame.quit()