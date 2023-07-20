import sys
n = list(map(int, sys.stdin.readline().split()))
x = []
for i in range(2):
  a = list(map(int, sys.stdin.readline().split()))
  for j in range(n[i]):
    x.append(a[j])
x.sort()
for i in x:
  print(i)