import re

text = """1. foo = 10 ;  bar  = 0.01; baz = 40
 236.   bar = 0.01;   baz= 30.1; foo =20.5
  42. foo= 0.5;  bar=10;  baz=900"""

lines = text.split("\n")
regex = re.compile(r"""
                   # Число в начале каждой строки
                   ^\s*\d+\.\s*
                   # Формат данных: XXX = NNM.MMM;
                   (\w+\s*=\s*\d+(?:\.\d+)?)\s*;\s*
                   (\w+\s*=\s*\d+(?:\.\d+)?)\s*;\s*
                   (\w+\s*=\s*\d+(?:\.\d+)?)\s*$""", re.VERBOSE)

for line in lines:
    match = regex.match(line)
    assert match is not None
    print(match.group(0))
    print(match.groups())
    print(match.group(1), match.group(2), match.group(3),
          sep=", ", end="\n\n")
