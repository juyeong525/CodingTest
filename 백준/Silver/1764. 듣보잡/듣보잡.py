import sys
n, m = map(int, sys.stdin.readline().split())
nh = set([sys.stdin.readline()[:-1] for _ in range(n)])
ns = set([sys.stdin.readline()[:-1] for _ in range(m)])
a = list(nh & ns)
print(len(a))
a.sort(key= lambda x: x)
for i in a:
  print(i)