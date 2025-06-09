# 1
from re import *

s = open("24.txt").readline()

reg = r"[ABC]+"

print(max([len(x.group()) for x in finditer(reg, s)]))

# 2 (ZX или ZY)

reg = r"(ZX|ZY)+" # пара повторяется н-ое кол-во раз
print(max([len(x.group()) // 2 for x in finditer(reg, s)])) # тк пары

# 3 (согл или гл)

reg = r"([BCD][AO])+"
print(max([len(x.group()) // 2 for x in finditer(reg, s)]))

# 4 (АА или СС) (пересечения)

from re import *

s = open("24.txt").readline()

reg = r"(AA|CC)+"
reg = rf"(?=({reg}))"

print(max([len(x.group(1)) // 2 for x in finditer(reg, s)]))


# 5
from re import *

s = open("24.txt").readline()

reg = r"([123][ABC][123])+"
reg = rf"(?=({reg}))"
print(max([len(x.group(1)) for x in finditer(reg, s)]))

# 6
from re import *

s = open("24.txt").readline()

reg = r"(YZZ|XY|YZ)"
reg = rf"(?=({reg}))"
print(max([len(x.group(1)) // 3 for x in finditer(reg, s)]))

# АРИФМЕТИЧЕСКИЕ ВЫРАЖЕНИЯ

# 7 

from re import *

s = open("24.txt").readline()

num = r"([1-9][0-9]*)"
reg = rf"{num}([-*]{num})+"

m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)

# 8 (целые неотр., троичные числа)

from re import *

s = open("24.txt").readline()

num = r"([12][012]*|0)"
reg = rf"{num}([+*]{num})*"

m = max([x.group() for x in finditer(reg, s), key = len])
print(len(m), m)

# 9 (выражение, значение равно нулю)

from re import *
s = open("24.txt").readline()

num = r"([1-9][0-9]*|0)"
proiz = rf"(({num}\*)*0(\*{num})*)"
reg = rf"{proiz}(\+{proiz})*"

m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)

# 10 (начинаются AF)

from re import *
s = open("24.txt").readline()

num = r"([1-9][0-9]*|0)"
reg = rf"AF{num}([+*]{num})*"

m = max([x.group() for x in finditer(reg, s)])
print(len(m), m)
