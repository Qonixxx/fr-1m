def f(x):
    s = ""
    while x:
        # s += str(x % 3) не писать.
        s = str(x % 3) + s
        x = x // 3
    return s

ans = []
for n in range(1, 1000):
    s = f(n)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        ost = (n % 3) * 5
        s = s + f(ost)
    r = int(s, 3)
    if r > 133:
        ans.append(r)
print(min(ans))

