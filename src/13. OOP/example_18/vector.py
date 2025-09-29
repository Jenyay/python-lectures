from math import sqrt

class Vector2D:
    """Класс вектора на плоскости"""
    def __init__(self, x1, y1, x2, y2):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)

    def __str__(self):
        return f"{self.p1} -> {self.p2}"

    @property
    def coord(self):
        return (self.p2[0] - self.p1[0], self.p2[1] - self.p1[1])

    def __abs__(self):
        coord = self.coord
        return sqrt(coord[0]**2 + coord[1]**2)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return self.coord == other.coord

    def __add__(self, other):
        delta = other.coord
        x2 = self.p2[0] + delta[0]
        y2 = self.p2[1] + delta[1]
        return Vector2D(self.p1[0], self.p1[1], x2, y2)

    def __sub__(self, other):
        delta = other.coord
        x2 = self.p2[0] - delta[0]
        y2 = self.p2[1] - delta[1]
        return Vector2D(self.p1[0], self.p1[1], x2, y2)
