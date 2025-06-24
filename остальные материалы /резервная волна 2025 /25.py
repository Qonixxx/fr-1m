def div(x): return sorted({i for d in range(1, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
def prime(x): return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
k = 0

for x in range(6651220, 10 ** 7):
    if k == 5: break
    xs = [i for i in div(x) if prime(i) and str(i).count("2") == 1]
    if len(xs) != 0:
        for q in range(len(xs)):
            if xs[q] * xs[q] == x:
                print(x, xs[q])
                k += 1
        for i in range(len(xs)):
            for j in range(len(xs) - 1):
                if xs[i] * xs[j] == x:
                    if xs[i] > xs[j]:
                        print(x, xs[i])
                    else:
                        print(x, xs[j])
                    k += 1
