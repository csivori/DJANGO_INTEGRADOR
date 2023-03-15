def get_int()->int:
  num = input("Ingrese un número: ")
  while True:
    num = input("Re-Ingrese un NUMERO: ")
    try:
      num = int(num)
      return num
    except ValueError:
      pass
  
print(get_int())