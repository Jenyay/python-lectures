class Vector2D:
    """Класс вектора на плоскости"""
    def __init__(self, x1, y1, x2, y2):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)

    def __str__(self):
        return f"{self.p1} -> {self.p2}"
