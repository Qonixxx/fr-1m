ans = []
xs = [int(x) for x in open("17.txt")]

def ch1(x, y, z): return (x > 0 and y > 0 and z > 0) or \
    (x < 0 and y < 0 and z < 0)
def ch2(x): return 100 <= abs(x) <= 999 and abs(x) % 100 == 15

mn = min(x for x in xs if ch2(x))

for x, y, z in zip(xs, xs[1:], xs[2:]):
    if ch1(x, y, z) and max([x, y, z]) * min([x, y, z]) > mn ** 2:
        ans.append(max([x, y, z]) * min([x, y, z]))
print(len(ans), min(ans))
