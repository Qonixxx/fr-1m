# задача с апробацией (14 мая)

# регулярки
from re import *

s = open("24.txt").readline()

re = r'[1-9AB][0-9AB]+[13579B]' # только от последней цифры зависит чётность числа, тк совокупность всех разряядов до этого кратна 12

m = max((x.group(0) for x in finditer(reg, s)), key = lambda x: int(x, 12))

print(s.find(m)) # находит первое вхождение в строке


# двойной цикл
s = open("24.txt").readline()
for c in "QWERTYUIOPSDFGHJKLZXCVNM": s = s.replace(c, " ")

m = 1
for l in range(len(s)):
  for r in range(l + m - 1, len(s)): # l + m - 1 нужен из-за того, что из-за первого вхождения макс. строки длиной 109 не учитываются последующие, тк следующий цикл начинается со 110
    c = s[l:r + 1]
    if c[0] == "0" or " ": break
    if c[-1] in "13579B": 
      m = max(m, len(c))
      if len(c) == 109: print(c, l)
