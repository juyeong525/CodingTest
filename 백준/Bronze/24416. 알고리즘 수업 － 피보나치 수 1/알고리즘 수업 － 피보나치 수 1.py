n = int(input())
f = [0] * (n+1)
def fibonacci(n):
  cnt = 0
  f[1] = f[2] = 1
  for i in range(3,n+1):
    f[i] = f[i - 1] + f[i - 2]  # 코드2
    cnt += 1
  return cnt
result = fibonacci(n)
print(f[n], result)