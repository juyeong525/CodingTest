import sys
x = [int(sys.stdin.readline()) for _ in range(5)]
print(sum(x)//5)
x.sort()
print(x[2])