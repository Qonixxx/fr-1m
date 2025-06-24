from re import *
mx = 0
s = open("24.txt").readline()
for c in "02468": s = s.replace(c, "2")
for x in "QWERTYUIOPASDFGHJKLZXCVBNM":
    reg = rf"[2][{x}]+[2]"
    m = max([x.group(0) for x in finditer(reg, s)], key = len)
    if len(m) > mx: mx = len(m)
print(mx)
