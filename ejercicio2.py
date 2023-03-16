def esPrimo(num:int)->bool:
  '''Dado un número, retorna 'true' si es Primo o 'false' si no lo es'''
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def obtenerProximoPrimo(num:int)->int:
  '''Dado un número, retorna el próximo numero Primo'''

  num = num + 1
  while (not esPrimo(num)):
    num = num + 1
  return num

def mcm(num:int)->list:
  '''Dado un número, retorna una lista con el Mínimo Común Múltiplo'''
  
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
