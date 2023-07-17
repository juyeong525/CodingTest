import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
  a = list(sys.stdin.readline().split())
  if a[0] == "push":
    x.append(int(a[1]))
  elif a[0] == "top":
    if len(x) != 0:
      print(x[-1])
    else:
      print(-1)
  elif a[0] == "size":
    print(len(x))
  elif a[0] == "empty":
    if len(x) != 0:
      print(0)
    else:
      print(1)
  else:
    if len(x) != 0:
      print(x[-1])
      x.pop()
    else:
      print(-1)