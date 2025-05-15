# задача на кубические коробки с условмем, что одну коробку можно вложить в другую, если её размер меньше другой на K едениц, и цвета отличаются

with open("26.txt") as f:
  M, K = [int(x) for x in f.readline().split()]

# стандартная процедура заполнения списка в 26-х
boxes = []
for s in f:
  size, color = s.split()
  boxes.append([int(size), color])
boxes.sort(reverse = 1) # выгодно "развернуть" список, тк в последствии станет удобно работать с парами

mx = [0] * N

for i in range(N):
  previous = [mx[j] for j in range(i) if boxes[j][0] - boxes[i][0] >= K and boxes[i][1] != boxes[j][1]]
  if previous:
    mx[i] = max(previous) + 1
  else:
    mx[i] = 1

mxans = max(mx)
print(mxans, [boxes[i][0] for i in range(N) if mx[i] == mxans])
