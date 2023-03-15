def esPrimo(num:int)->bool:
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def obtenerProximoPrimo(num:int)->int:
  num = num + 1
  while (not esPrimo(num)):
    num = num + 1
  return num

def mcm(num:int)->list:
  mcm = []
  multiplo = 2
  while (multiplo <= num):
    if (num % multiplo == 0):
      mcm.append(multiplo)
      num = num / multiplo
    else:
      multiplo = obtenerProximoPrimo(multiplo)
  return mcm

print(mcm(140))
