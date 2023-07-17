import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
  a = int(sys.stdin.readline())
  if a == 0:
    x.pop()
  else:
    x.append(a)
print(sum(x))