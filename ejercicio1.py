def mcd(num1:int, num2:int)->int:
  '''Retorna un entero con el Máximo Común Divisor a partir de 2 números enteros dados'''
  
  divisor = int(min(num1, num2) / 2)
  while (divisor > 1):
    if (num1 % divisor == 0) and (num2 % divisor == 0):
      return divisor
    divisor = divisor - 1
  return 1

print(mcd(100, 240))