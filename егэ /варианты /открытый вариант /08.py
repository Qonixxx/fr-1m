from itertools import *
k = 0
for x in permutations("0123456789", 4):
    s = "".join(x)
    for x in "468": s = s.replace(x, "2")
    for y in "3579": s = s.replace(y, "1")
    if s[0] != "0" and "11" not in s and "02" not in s and "20" not in s and "22" not in s:
        k += 1
print(k)
