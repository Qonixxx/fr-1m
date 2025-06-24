ans = []
def f(x):
    s = ""
    while x:
        s = str(x % 3) + s
        x //= 3
    return s

for n in range(1, 1000):
    s = f(n)
    if n % 3 == 0:
        s = "1" + s + "02"
    else:
        ost = (n % 3) * 4
        ost = f(ost)
        s = s + ost
    r = int(s, 3)
    if r < 100:
        ans.append(n)
print(max(ans))
