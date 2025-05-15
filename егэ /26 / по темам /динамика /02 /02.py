# 21910 (КЕГЭ)
with open("26.txt") as f:
  n = int(f.readline())
  a = sorted([int(x) for x in f], reverse = True)

mxZep = [0] * n

for i in range(N):
  box = a[i]
  for j in range(i):
    prev = a[j]
    if prev - box >= 9:
      mxZep[i] = max(mxZep[i], mxZep[j] + 1)
  if mxZep[i] == 0: mxZep[i] = 1

print(max(mxZep), max(a[i] for i in range(n) if mxZep[i] == 1040))
