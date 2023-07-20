import sys
a = int(sys.stdin.readline())
x = []
for _ in range(a):
  s = sys.stdin.readline().split()
  x.append([int(s[0]),s[1]])
x.sort(key= lambda x: x[0])
for i in x:
  print(i[0],i[1])