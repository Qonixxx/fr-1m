'''
В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E. 
Найдите длину самой длинной подцепочки, состоящей из символов A, B или C (в произвольном порядке).
'''

from re import *

s = open("24.txt").readkine()

reg = r"[ABC]+" # набор символов A, B или C, идущих подряд

# как проверить работу регулярки

# print(s[:100])
# print([x.group() for x in finditer(reg, s[:100])])

print(max([len(x.group()) for x in finditer(reg, s)]))
