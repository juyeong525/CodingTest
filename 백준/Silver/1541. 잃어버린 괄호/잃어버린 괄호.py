result = [sum(list(map(int, x.split("+")))) for x in input().split("-")]
q = result[0]
for r in range(1, len(result)):
  q -= result[r]
print(q)