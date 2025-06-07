data = []

def density(count, H, W):
    return count / (H * W)

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def gkl(p0):
    kl = [p for p in data if dist(p0, p) < 1]
    if len(kl) > 0:
        for p in kl: data.remove(p)
        nkl = [gkl(p) for p in kl]
        for c in nkl: kl.extend(c)
    return kl

def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]

for s in open("27A.txt"): data.append([float(c) for c in s.split()])
print(len(data))

kls = []
stars_sums = []
while len(data) > 0:
    p0 = data.pop()
    kl = [p0] + gkl(p0)
    stars_sums.append(len(kl))
    print(len(kl))
    kls.append(kl)
print(len(kls))

centroids = [center(kl) for kl in kls]
densitys  = [density(stars_sums[i], 4, 4) for i in range(len(kls))]
px = sum(densitys) / len(kls)
py = dist(centroids[1], centroids[2])
print(int(px * 10 ** 3), int(py * 10 ** 3))
# print(centroids)
# print(densitys) второй и третий центр, второй больше  
