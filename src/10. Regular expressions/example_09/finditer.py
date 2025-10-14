import re

text = """1. foo = 10 ;  bar  = 0.01; baz = 40
 236.   bar = 0.01;   baz= 30.1; foo =20.5
  42. foo= 0.5;  bar=10;  baz=900"""

regex = re.compile(r"""
               # Число в начале каждой строки
               ^\s*\d+\.\s*
               # Формат данных: XXX = NNM.MMM;
               (?:(?P<name1>\w+)\s*=\s*(?P<val1>\d+(?:\.\d+)?))\s*;\s*
               (?:(?P<name2>\w+)\s*=\s*(?P<val2>\d+(?:\.\d+)?))\s*;\s*
               (?:(?P<name3>\w+)\s*=\s*(?P<val3>\d+(?:\.\d+)?))\s*$""",
               re.VERBOSE | re.MULTILINE)

for match in regex.finditer(text):
    print(match.group(0))
    print(match.groupdict())
    print(f"{match.group('name1')} = {match.group('val1')}")
    print(f"{match.group('name2')} = {match.group('val2')}")
    print(f"{match.group('name3')} = {match.group('val3')}")
    print()
