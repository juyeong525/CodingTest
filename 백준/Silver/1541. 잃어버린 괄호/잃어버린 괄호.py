import sys
v = sys.stdin.readline().split("-")
v[-1] = v[-1][:-1]
result = []
for x in v:
  a = list(map(int, x.split("+")))
  result.append(sum(a))
q = result[0]
for r in range(1, len(result)):
  q -= result[r]
print(q)