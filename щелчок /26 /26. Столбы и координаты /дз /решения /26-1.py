with open("26.txt") as f:
    n, m, k = [int(x) for x in f.readline().split()]
    field = [m + 1] * (k + 1)

    for i in range(n):
        x, y = [int(x) for x in f.readline().split()]
        field[y] = min(field[y], x)
    ans = [0, 0]
    for i in range(1, k):
        mn = min(field[i], field[i + 1]) - 1
        if mn > ans[0] and mn > 0:
            ans = [mn, i]
        elif mn == ans[0] and mn > 0:
            ans[1] = min(ans[1]. i)
print(*ans)
