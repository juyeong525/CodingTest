import sys
n = int(sys.stdin.readline())
v = [-1] * n
count = 0
for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  if v[a[0]-1] != -1 and v[a[0]-1] != a[1]:
    count += 1
    v[a[0]-1] = a[1]
  else:
    v[a[0]-1] = a[1]
print(count)