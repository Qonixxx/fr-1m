from itertools import *
k = 0

for a in product("БАНДЕРОЛЬ", repeat = 7):
  s = "".join(a)
  for c in "БНДРЛ": s = s.replace(c, "Б")
  if s.count("Ь") <= 1 and "БЕ" not in s and "ЕБ" not in s:
    k += 1
print(k)
