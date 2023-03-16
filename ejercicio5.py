def get_int_iterativa()->int:
  '''Lee un valor entero de la consola, iterando mientras el valor no sea numérico (iterativamente)'''

  num = input("Ingrese un número: ")
  while True:
    try:
      num = int(num)
      return num
    except ValueError:
      num = input("ERROR: Debe ser un valor entero!   Ingrese un número: ")
  
def get_int_recursiva()->int:
  '''Lee un valor entero de la consola, iterando mientras el valor no sea numérico (recursivamente)'''
  
  num = input("Ingrese un número: ")
  try:
    num = int(num)
    return num
  except ValueError:
    print("ERROR: Debe ser un valor entero!   ", end='')
    return get_int_recursiva()

print(get_int_iterativa())
print(get_int_recursiva())