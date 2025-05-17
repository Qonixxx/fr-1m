# открытый вариант (2025)
from re import *

s = open("24.txt").readline()

reg = r'[1-9][0-9A-D]+[02468AC]'

m = max((x.group(0) for x in finditer(reg, s)), key = len)
print(len(m))
