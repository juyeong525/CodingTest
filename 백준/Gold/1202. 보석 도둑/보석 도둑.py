import sys, heapq
n, k = map(int, sys.stdin.readline().split())
x = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]
x.sort()
bags.sort()
tmp = []
result = 0
for bag in bags:
    while x and bag >= x[0][0]:
        heapq.heappush(tmp, -x[0][1])
        heapq.heappop(x)
    if tmp:
        result += heapq.heappop(tmp)
    elif not x:
        break
print(-result)