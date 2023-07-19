import sys
from collections import deque
x = deque()
for i in range(1, int(sys.stdin.readline()) + 1):
  x.append(i)
while(len(x) != 1):
  x.popleft()
  x.append(x.popleft())
print(x[0])