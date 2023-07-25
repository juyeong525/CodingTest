import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
result = []
sum1 = 0
for i in a:
    sum1 += i
    result.append(sum1)
print(sum(result))