from sys import *
setrecursionlimit(100000)

def f(n): return n if n >= 2025 else n * 2 + f(n + 2)
print(f(82) - f(81))
