k = 0
for s in open("26.txt"):
    xs = sorted([int(x) for x in s.split()])
    if len(xs) == len(set(xs)):
        if xs[-1] + xs[-2] <= sum(xs) - xs[-1] - xs[-2]:
            k += 1
print(k)
