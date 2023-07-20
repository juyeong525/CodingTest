import sys
n = list(map(int, sys.stdin.readline().split()))
x = list(map(int, sys.stdin.readline().split()))
x.sort(reverse=True)
print(x[n[1]-1])