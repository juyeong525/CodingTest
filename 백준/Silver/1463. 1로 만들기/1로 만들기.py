def number1463(n):
  f = [0] * (n+1)
  f[0] = f[1] = 0
  for i in range(2,n+1):
    f[i]  = f[i - 1] + 1
    if i % 3 == 0:
      f[i] = min(f[i], f[i // 3] + 1)
    if i % 2 == 0:
      f[i] = min(f[i], f[i // 2] + 1)
  return f[n]
print(number1463(int(input())))