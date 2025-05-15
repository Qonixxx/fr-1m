k = 0
for x in range(2030 + 1):
    s = 7 ** 350 + 7 ** 150 - x
    xs = []
    while s:
        xs += [s % 7]
        s //= 7
    if xs.count(0) == 200: print(x)
