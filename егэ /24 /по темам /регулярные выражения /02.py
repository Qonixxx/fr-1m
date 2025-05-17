'''
Текстовый файл состоит из символов А, В и С.

Определите максимальное количество идущих подряд пар символов АВ или АС в прилагаемом файле.
'''

from re import *

s = open("24.txt").readline()

reg = r"(ZX|ZY)"

print(max(len(x.group()) // 2 for x in finditer(reg, s)))

