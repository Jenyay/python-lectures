from vector import Vector2D

AB = Vector2D(1, 1, 2, 2)

CD = AB * 2
print("CD:", CD)

print(f"{id(AB)=}")
AB *= 3

print("AB *= 3")
print("AB:", AB)
print(f"{id(AB)=}")
