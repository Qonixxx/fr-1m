s = 15 * 2401 ** 1500 - 10 * 343 ** 1200 + 40 * 49 ** 1000 - 15 * 7 ** 850 - 4805
xs = []
while s:
  xs += [s % 49]
  s //= 49
k = 0
for i in range(9, 48):
  k += xs.count(i)
print(k)
