import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
  x.append(int(sys.stdin.readline()))
x.sort()
for j in x:
  print(j)