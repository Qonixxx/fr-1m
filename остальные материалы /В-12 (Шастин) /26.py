with open("26.txt") as f:
    n = int(f.readline())
    xs = []
    for i in range(n):
        x, y, t = [int(x) for x in f.readline().split()]
        xs.append([x, y, t])
xs.sort()

k = 0
a = []
for i in range(len(xs) - 1):
    x1, y1, t1 = xs[i]
    x2, y2, t2 = xs[i + 1]
    if x1 == x2 and y1 == y2:
        a.append([x1, y1, t1])
        a.append([x2, y2, t2])

times = []
res = []
for row in a:
    if row[2] not in times:
        res.append(row)
        times.append(row[2])
# [print(row) for row in res]

ans = []
mn = float("inf")
for i in range(len(res) - 1):
    x1, y1, t1 = res[i]
    x2, y2, t2 = res[i + 1]
    if x1 == x2 and y1 == y2:
        if (t2 - t1) < mn:
            mn = t2 - t1
            if mn == 53:
                ans.append([x1, y1])
                
print(sum(ans[0]), mn)
    
