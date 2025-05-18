ans = []
xs = [int(x) for x in open("17.txt")]
mx = max([x for x in xs if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 17])
def ch1(x): return x % 100 != 17

for x, y, z in zip(xs, xs[1:], xs[2:]):
  if not((ch1(x)) and (ch1(y)) and ch1(z)) and (abs(x) + abs(y) + abs(z)) <= mx:
    ans.append(x + y + z)
print(len(ans), min(ans))
