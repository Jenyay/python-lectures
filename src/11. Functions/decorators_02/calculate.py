def calculate(action, *args):
    result = action(*args)
    params_text_items = [str(arg) for arg in args]
    params_text = ", ".join(params_text_items)
    print(f"{action.__name__}({params_text}) = {result}")
    return result

def add(a, *args):
    return a + sum(args)

def mul(a, *args):
    result = a
    for n in args:
        result *= n
    return result

foo = calculate(add, 2, 3, 4, 5)
print(f"{foo=}")
bar = calculate(mul, 2, 3, 4)
print(f"{bar=}")
