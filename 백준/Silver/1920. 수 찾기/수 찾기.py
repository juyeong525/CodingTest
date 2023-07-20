import sys
a = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
a1 = int(sys.stdin.readline())
x1 = list(map(int, sys.stdin.readline().split()))
result = set(x) & set(x1)
for i in x1:
  if i in result:
    print(1)
  else:
    print(0)