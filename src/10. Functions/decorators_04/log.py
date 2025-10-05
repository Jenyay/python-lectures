def log_func(action):
    def calculate(*args, **kwargs):
        result = action(*args, **kwargs)
        action_name = action.__name__

        params_text_items = [str(arg) for arg in args]
        params_text_items += [f"{str(key)}={str(value)}" 
                              for key, value in kwargs.items()]

        params_text = ", ".join(params_text_items)
        print(f"{action_name}({params_text}) = {result}")
        return result
    return calculate

def add(a, *args, **kwargs):
    return a + sum(args)

def mul(a, *args, **kwargs):
    result = a
    for n in args:
        result *= n
    return result

add = log_func(add)
mul = log_func(mul)

foo = add(2, 3, 4, 5, arg1=10, arg2=20)
print(f"{foo=}")
bar = mul(2, 3, 4, arg1=10, arg2=20)
print(f"{bar=}")
