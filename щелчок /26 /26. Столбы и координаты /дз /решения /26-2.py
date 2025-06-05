with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([int(x) for x in f], reverse = True)
    
ans = [xs[0]]
for i in range(1, n):
    if ans[-1] - xs[i] >= 8:
        ans.append(xs[i])
print(len(ans), ans[-1])
