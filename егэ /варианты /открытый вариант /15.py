def f(x, a):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (not(x & a == 0))

for a in range(1, 300):
    if all(f(x, a) == 1 for x in range(1, 300)):
        print(a)
