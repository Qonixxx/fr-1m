# 1
s = open("24.txt").readline()

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if "D" not in c:
            m = max(m, len(c))
        else: break
print(m)


# 2

s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if all(c[i] != c[i + 1] for i in range(len(c) - 1)):
            m = max(m, len(c))
        else:
            break
print(m)

# 3
s = open("24.txt").readline()

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if all(c[i] + c[i + 1] + c[i + 2] != c[i + 3] + c[i + 4] + c[i + 5] for i in range(len(c) - 5)):
            m = max(len(c), m)
        else:
            break
print(m)

# 4 (пары ZX или ZY)

s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if all(c[i] + c[i + 1] in ["ZX", "ZY"] for i in range(0, len(c), 2)):
                m = max(m, len(c))
            else:
                break
print(m // 2)

# * (регулярка)
from re import *
reg = r"(ZX|ZY)+" # пара повторяется н-ое кол-во раз
print(max([len(x.group()) // 2 for x in finditer(reg, s)])) # тк пары

# 5

s = open("24.txt").readline()
s = s.replace("B", "A").replace("C", "A").replace("2", "1").replace("3", "1")
m = 0

for l in range(len(s)):
    for r in range(l + m. len(s)):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if all(c[i] + c[i + 1] == "A1" for i in range(0, len(c), 2)):
                m = max(m, len(c))
            else:
                break
print(m // 2)


# МЕТОД ДВУХ УКАЗАТЕЛЕЙ

# 6

s = open("24.txt").readline()
m = 0

for l in range(len(c)):
    for r in range(l + m, len(c)):
        c = s[l:r + 1]
        if c.count("A") <= 5:
            m = max(m, len(c))
        else:
            break
print(m)

# 7
s = open("24.txt").readline()
m = 10000

for l in range(len(s)):
    for r in range(l, l + m):
        c = [l:r + 1]
        if c.count(".") == 7:
            m = min(m, len(c))
            break
print(m)

# 8
s = open("24.txt").readline()
m = 10000

for l in range(len(s)):
    for r in range(l + 2, l + m):
        c = s[l:r + 1]
        if c[0] != "A": break
        if c[0] == "A" and c[-1] == "F":
            m = min(m, len(c))
            break
print(m)


# 9
s = open("24.txt").readline()

for c in "QWERTYUIOPSJKLZXVBNM00": s = s.replace(c, " ")

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = [l:r + 1]
        if c[0] != "0" and " " not in c:
            m = max(m, len(c))
        else:
            break
print(m)

# 10 (досрок 2025)

s = open("24.txt").readline()

for c in "QWERTYUIOPSDFGHJKLZXCVNM": s = s.replace(c, " ")

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = [l:r + 1]
        if c[0] != "0" and " " not in s:
            if c[-1] in "02468A": m = max(m, len(c))
        else:
            break
print(m)
