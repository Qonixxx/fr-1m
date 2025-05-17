original = 1024 * 768 * 23
compress = 800 * 600 * 22
difference = original - compress
ans = difference * 100 / 2 ** 13
print(ans)
