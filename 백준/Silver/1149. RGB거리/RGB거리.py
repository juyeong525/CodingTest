n = int(input())
v = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
  v[i][0] += min(v[i-1][1], v[i-1][2])
  v[i][1] += min(v[i-1][0], v[i-1][2])
  v[i][2] += min(v[i-1][1], v[i-1][0])
print(min(v[-1]))