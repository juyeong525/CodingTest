import sys
n = int(sys.stdin.readline())
x = sys.stdin.readline().split()
m = int(input())
y = sys.stdin.readline().split()
s = set(x) & set(y)
for k in y:
  if k in s:
    print(1)
  else:
    print(0)