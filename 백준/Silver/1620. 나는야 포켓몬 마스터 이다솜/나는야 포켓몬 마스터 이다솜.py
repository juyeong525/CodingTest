import sys
n, m = map(int, sys.stdin.readline().split())
x = [sys.stdin.readline()[:-1] for _ in range(n)]
for _ in range(m):
  a = sys.stdin.readline()
  try:
    print(x[int(a)-1])
  except:
    print(x.index(a[:-1])+1)