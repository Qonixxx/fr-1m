def f(s, e):
  if s > e or s == 16: return 0
  if s == e: return 1 
  return f(s + 2, e) + f(s + 3, e) + f(s ** 2, e)
print(f(2, 25) * f(25, 42))
