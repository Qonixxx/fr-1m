def f(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s # нельзя писать s += str(x % 3)
        x //= 3
    return s

for n in range(3, 200):
    s = f(n)
    if n % 3 == 0: 
        s += s[-2:]
    else: 
        s += f((n % 3) * 3)
    r = int(s, 3)
    if r <= 150: 
        print(n)
