# 26 на динамику

# 1 (на куб. коробки)
with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([int(x) for x in f], reverse = True)

max_zep = [0] * N

for i in range(i):
    box = xs[i]
    for j in range(i):
        prev_box = xs[j]
        if prev_box - box == 9:
            max_zep[i] = max(max_zep[i], max_zep[j] + 1)
    if mxzep[i] == 0: mxzep[i] == 1
print(max(max_zep), max(a[i] for i in range(n) if max_zep[i] == 1040))

# ---------------------------------------------------------------------------------

# 2 (куб. коробки (цвет))
with open("26.txt") as f:
    N, K = [int(x) for x in f.readline().split()]

a = [] # коробки
for s in f:
    size, color = s.split()
    boxes.append([int(size), color])
    boxes.sort(reverse = 1)

max_zep = [0] * N

for i in range(N):
     prev_zep = [max_zep(j) for j in range(i) if a[j][0] - a[i][0] == 9 and a[j][1] != a[i][1]]
     if prev_zep:
         max_zep[i] = max(prev_zep) + 1
     else:
         max_zep[i] += 1
mx = max(max_zep)
print(mx, [a[i][0] for i in range(N) if max_zep[i] == mx])


# -----------------------------------------------------------------------------------


# 3 (на путешествия в зоны)

with open("26.txt") as f:
    n, k = [int(x) for x in f,readline().split()]

    xs = [] # все поездки
    for s in f:
        frm, to, price = [int(x) for x in s.split()]
        xs.append([frm, to, price])
    xs.sort()

min_price = [10 ** 10] * 10 ** 6
min_price[1] = 0
for i in range(n):
    frm, to, price = xs[i]
    sum_price = min_price[frm] + price
    if sum_price <= k:
        min_price[to] = max(min_price[to], sum_price)
ans1 = max(i for i in range(10 ** 6) if min_price[i] != 10 ** 10)
print(ans1, k - min_p[ans1])

# -----------------------------------------------------------------------------------


# 4 (макс. длительность + аренда)
with open("26.txt") as f:
    n = int(f.readline())
    xs = []
    for s in f:
        st, end, price = [int(x) for x in s.split()]
        xs.append([st, end, price])
    xs.sort(key = lambda x: x[1])

max_dlit = [(0, 0)] * n

for i in range(n):
    pred_dlit = [max_dlit[j] for j in range(i) if xs[i][0] > xs[j][1]]
    if pred_dlit:
        s, p = max(pred_dlit)
        max_dlit[i] = (s + xs[i][1] - xs[i][0] + 1, p + xs[i][2])
    else:
        max_dlit[i] = (xs[i][1] - xs[i][0] + 1, p + xs[i][2])
print(max(max_dlit))
