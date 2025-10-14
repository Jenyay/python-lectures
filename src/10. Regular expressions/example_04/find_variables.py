import re

text_correct = """1. foo = 10 ;  bar  = 0.01; baz = 40
 236.   bar = 0.01;   baz= 30.1; foo =20.5
31.  bar=0.01;  foo = 30 ; baz =25.5
  42. foo= 0.5;  bar=10;  baz=900"""

text_invalid = """bar=0.01; baz=30; foo=10.2
5B. bar=0.01; baz=30; foo=10
1. bar=0.01; baz=30; foo=10 spam=10
52. fmin=0.01 fmax=30 D=10"""

lines_correct = text_correct.split("\n")
lines_invalid = text_invalid.split("\n")

regex = re.compile(r"""
                   # Число в начале каждой строки
                   ^\s*\d+\.\s*
                   # Формат данных: XXX = NNM.MMM;
                   (\w+\s*=\s*\d+(\.\d+)?)\s*;\s*
                   (\w+\s*=\s*\d+(\.\d+)?)\s*;\s*
                   (\w+\s*=\s*\d+(\.\d+)?)\s*$""", re.VERBOSE)

for line in lines_correct:
    match = regex.match(line)
    assert match is not None

for line in lines_invalid:
    match = regex.match(line)
    assert match is None
