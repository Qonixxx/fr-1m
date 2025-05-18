def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x//d}})
k = 0

for x in range(424242, 10 ** 7):
  if k == 8: break
  xs = div(x)
  if xs:
    M = xs[0] + xs[-1]
    if M % 2024 == 42:
      print(x, M)
      k += 1 
