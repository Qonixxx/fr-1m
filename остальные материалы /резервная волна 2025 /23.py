def f(s, e):
    if s == 10 or s > e: return 0
    if s == e: return 1
    return f(s + 1, e) + f(s + 2, e) + f(s * 2, e)
print(f(3, 7) * f(7, 20))
