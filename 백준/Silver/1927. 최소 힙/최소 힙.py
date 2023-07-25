from heapq import heappush, heappop
import sys
v = []
n = int(sys.stdin.readline())
for i in range(n):
  a = int(sys.stdin.readline())
  if a != 0:
    heappush(v, a)
  else:
    try:
      print(heappop(v))
    except:
      print(0)