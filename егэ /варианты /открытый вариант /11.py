from math import *

for kod in range(1, 100):
    bit = ceil(log2(kod))
    byte = ceil(246 * bit / 8)
    if byte * 703569 <= 77 * 1024 * 1024:
        print(kod)
