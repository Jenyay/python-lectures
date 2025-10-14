import re

text = """1. foo = 10 ;  bar  = 0.01; baz = 40
 236.   bar = 0.01;   baz= 30.1; foo =20.5
  42. foo= 0.5;  bar=10;  baz=900"""

regex = re.compile(r"""(?:(?P<name>\w+)\s*=\s*(?P<val>\d+(?:\.\d+)?))""",
                   re.MULTILINE)

for match in regex.finditer(text):
    print(match.groupdict())
