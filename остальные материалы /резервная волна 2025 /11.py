from math import *

for l in range(1, 100):
    kod = 10 + 17
    char = ceil(log2(kod))
    num = ceil(char * l / 8)
    if num * 7564230 > 31 * 2 ** 20:
        print(l)
