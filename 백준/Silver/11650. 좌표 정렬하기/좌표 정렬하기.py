import sys
a = int(sys.stdin.readline())
x = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
x.sort(key= lambda x: [x[0], x[1]])
for i in x:
  print(i[0],i[1])