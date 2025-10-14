import re

text = """1. foo = 10 ;  bar  = 0.01; baz = 40
236.   bar = 0.01;   baz= 30.1; foo =20.5
42. foo= 0.5;  bar=10;  baz=900"""

regex = re.compile(r"""(?:(\w+)\s*=\s*(\d+(?:\.\d+)?))""",
                   re.MULTILINE)

result = regex.sub(r"\1=\2", text)
print(result)
