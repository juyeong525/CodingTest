n, m = list(map(int, input().split()))
v = [int(input()) for _ in range(n)]
v.sort()
start = 1
end = max(v)
mid = 0
while start <= end:
  mid = (start + end) // 2
  lan = 0
  for vd in v:
    lan += vd // mid
  if lan < m:
    end = mid - 1
  else:
    start = mid + 1
print(end)