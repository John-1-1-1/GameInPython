class Turret:
    def __init__(self, angle=0, angular_speed=0):
        self.angle = angle  # Угол поворота дуло
        self.angular_speed = angular_speed

    def rotate(self, angular_speed):
        """Поворот дуло."""
        self.angle += self.angular_speed * (angular_speed // abs(angular_speed))

    def get_angle(self):
        """Получить текущий угол дуло."""
        return self.angle