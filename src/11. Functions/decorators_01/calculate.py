def calculate(a, b, action):
    result = action(a, b)
    action_name = action.__name__
    print(f"{action_name}({a}, {b}) = {result}")
    return result

def add(a, b): return a + b

def mul(a, b): return a * b

foo = calculate(2, 3, add)
print(f"{foo=}")
bar = calculate(2, 3, mul)
print(f"{bar=}")
