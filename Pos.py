import math

class Pos:
    def __init__(self, x=0, y=0, speed=0, angle=0, angular_speed=0):
        self.x = x          # Координата X
        self.y = y          # Координата Y
        self.speed = speed  # Скорость перемещения
        self.angle = angle  # Угол поворота в градусах
        self.angular_speed = angular_speed  # Угловая скорость в градусах за шаг

    def move(self):
        """Перемещение объекта с учетом угла и скорости."""
        # Преобразование угла в радианы
        rad = math.radians(self.angle)
        # Вычисление изменения координат
        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

    def rotate(self, angular_speed):
        """Поворот объекта с учетом угловой скорости."""
        self.angle += self.angular_speed * (angular_speed // abs(angular_speed))
        # Убедимся, что угол остается в пределах 0-360 градусов
        self.angle %= 360

    def __str__(self):
        """Строковое представление объекта Pos."""
        return f"Pos(x={self.x}, y={self.y}, speed={self.speed}, angle={self.angle}, angular_speed={self.angular_speed})"


if __name__ == "__main__":
    position = Pos(100, 200, speed=5, angle=45, angular_speed=10)
    # Перемещение и поворот объекта
    position.move()
    position.rotate()
    print(position)  # Выводит новые координаты и угол после перемещения и поворота