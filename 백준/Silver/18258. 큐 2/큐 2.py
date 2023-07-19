import sys
from collections import deque
x = deque()
for i in range(int(sys.stdin.readline())):
  a = sys.stdin.readline().split()
  if a[0] == "push":
    x.append(int(a[1]))
  elif a[0] == "pop":
    if len(x) != 0:
      print(x.popleft())
    else:
      print(-1)
  elif a[0] == "size":
    print(len(x))
  elif a[0] == "empty":
    if len(x) != 0:
      print(0)
    else:
      print(1)
  elif a[0] == "front":
    if len(x) != 0:
      print(x[0])
    else:
      print(-1)    
  else:
    if len(x) != 0:
      print(x[len(x)-1])
    else:
      print(-1)