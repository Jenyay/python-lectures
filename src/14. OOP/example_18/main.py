from vector import Vector2D

AB = Vector2D(1, 1, 2, 2)
CD = Vector2D(2, 2, 4, 4)

print("AB:", AB)
AB += CD
print("AB += CD")
print("AB:", AB)
