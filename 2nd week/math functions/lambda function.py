x = lambda a, b : a * b
print(x(1, 8))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))