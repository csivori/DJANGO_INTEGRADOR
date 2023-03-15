def mcd(num1, num2:int)->int:
  '''
  '''
  divisor = int(min(num1, num2) / 2)
  while (divisor > 1):
    if (num1 % divisor == 0) and (num2 % divisor == 0):
      return divisor
    divisor = divisor - 1
  return 1

print(mcd(100, 240))