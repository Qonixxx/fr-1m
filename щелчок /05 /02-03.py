for n in range(256):
    s = bin(n)[2:].zfill(8)
    s = s.replace("0", "*")
    s = s.replace("1", "0")
    s = s.replace("*", "1")
    r = int(s, 2)
    if r - n == 113:
        print(n)

# -------------------------------------------------------------

ans = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        ost = (n % 3) * 3
        s = s + bin(ost)[2:]
    r = int(s, 2)
    if r >= 120:
        ans.append(n)
print(min(ans))
