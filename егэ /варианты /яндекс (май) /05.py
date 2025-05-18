'''
def c3(n):
  s = ""
  while n > 0:
    s = str(n % 3) + s
    n //= 3
  return s
'''
def c3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

for n in range(10000):
  s = c3(n)
  if sum(map(int, s)) % 2 == 0:
    s = "2" + s[2:] + "0"
  else:
    s = "20" + s[2:] + "1"
  r = int(s, 3)
  if r == 78:
    print(r, n)
