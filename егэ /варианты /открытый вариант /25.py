def div(x): return sorted({i for d in range(1, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
k = 0

for x in range(10 ** 5 * 5, 10 ** 6):
    if k == 5: break
    if sum(div(x)) % 10 == 6:
        print(x, sum(div(x)))
        k += 1
