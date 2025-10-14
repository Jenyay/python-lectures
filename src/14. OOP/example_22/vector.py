from math import hypot, isclose

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
        return hypot(*self.coord)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        self_coord = self.coord
        other_coord = other.coord
        return (isclose(self_coord[0], other_coord[0]) and
                isclose(self_coord[1], other_coord[1]))

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

    def __iadd__(self, other):
        delta = other.coord
        x2 = self.p2[0] + delta[0]
        y2 = self.p2[1] + delta[1]
        self.p2 = (x2, y2)
        return self

    def __isub__(self, other):
        delta = other.coord
        x2 = self.p2[0] - delta[0]
        y2 = self.p2[1] - delta[1]
        self.p2 = (x2, y2)
        return self

    def __mul__(self, n):
        coord = self.coord
        x2 = self.p1[0] + n * coord[0]
        y2 = self.p1[1] + n * coord[1]
        return Vector2D(self.p1[0], self.p1[1], x2, y2)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __imul__(self, n):
        coord = self.coord
        x2 = self.p1[0] + n * coord[0]
        y2 = self.p1[1] + n * coord[1]
        self.p2 = (x2, y2)
        return self
