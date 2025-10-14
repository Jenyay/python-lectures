from functools import wraps

def log_func(action):
    @wraps(action)
    def calculate(*args, **kwargs):
        result = action(*args, **kwargs)
        action_name = action.__name__

        params_text_items = [str(arg) for arg in args]
        params_text_items += [f"{str(key)}={str(value)}" 
                              for key, value in kwargs.items()]

        params_text = ", ".join(params_text_items)
        print(f"{action_name}({params_text}) = {result}")
        return result

    return  calculate

@log_func
def add(a, *args, **kwargs):
    """Функция возвращает сумму ее параметров."""
    result = a
    for n in args:
        result += n
    return result

@log_func
def mul(a, *args, **kwargs):
    """Функция возвращает произведение ее параметров."""
    result = a
    for n in args:
        result *= n
    return result

foo = add(2, 3, 4, 5, arg1=10, arg2=20)
print(f"{foo=}")
bar = mul(2, 3, 4, arg1=10, arg2=20)
print(f"{bar=}")

print(f"{add.__name__=}")
print(f"{add.__doc__=}")
print(f"{mul.__name__=}")
print(f"{mul.__doc__=}")
