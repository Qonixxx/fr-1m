# конф.зал
with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([list(map(int, i.split())) for i in f], key = lambda x: (x[1], x[0]))

hall = [xs.pop(0)]
for conf in xs:
    if conf[0] >= hall[-1][1]:
        hall.append(conf)
print(len(hall), hall[-2][1])
