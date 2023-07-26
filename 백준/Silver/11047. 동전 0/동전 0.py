import sys
n, k = map(int, sys.stdin.readline().split())
x = []
count = 0
for _ in range(n):
  r = int(sys.stdin.readline())
  if r <= k:
    x.append(r)
for i in range(len(x)-1, -1, -1):
  count += k // x[i]
  k %= x[i]
print(count)