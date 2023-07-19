import sys
n = list(map(int, sys.stdin.readline().split()))
x = [i for i in range(1, n[0]+1)]
gap = n[1]
n[1] -= 1
print("<", end="")
while len(x) != 1:
  print(x[n[1]], end=", ")
  if n[1] == len(x):
    x.remove(x[n[1]])
    n[1] = 1
  else:
    x.remove(x[n[1]])
  n[1] = (n[1] -1 + gap) % len(x)
print(x[0],end="")
print(">")