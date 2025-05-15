with open("26.txt") as f:
    n, l, m = map(f.readline().split())
    xs = []
    for i in range(n):
        st, r, t = f.readline().split()
        xs.append([int(st), int(st) + int(r), t])
xs.sort()

park = [0] * (L + M)
bus = out = 0
for i in range(n):
    st, end, t = xs[i]
    if t == "A":
        for j in range(L + M):
            if st <= park[j]:
                park[j] = end
                break
        else: out += 1
    if t == "B":
        for j in range(L, L + M):
            if st <= park[j]:
                park[j] = end
                bus += 1
                break
        else: out += 1
        
print(bus, out)
