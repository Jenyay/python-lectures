import re

text = """1. foo = 10 ;  bar  = 0.01; baz = 40
236.   bar = 0.01;   baz= 30.1; foo =20.5
42. foo= 0.5;  bar=10;  baz=900"""

regex = r"""(?:(?P<name>\w+)\s*=\s*(?P<val>\d+(?:\.\d+)?))"""
result = re.sub(regex, r"\g<name>=\g<val>", text, flags=re.MULTILINE)
print(result)
