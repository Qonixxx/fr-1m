with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([int(x) for x in f], reverse = True)

ans = []
ans.append(xs[0])
for i in range(1, len(xs)):
    if ans[-1] - xs[i] >= 9: ans.append(xs[i])
print(len(ans), ans[-1])
