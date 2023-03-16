def contadorDePalabras(cadena:str)->dict:
  '''Dada una cadena, devuelve un diccionario con la cantidad de veces que aparece cada palabra'''
  
  listaDePalabras = cadena.split(" ")
  diccionario = {}
  for palabra in listaDePalabras:
    if palabra in diccionario:
      diccionario[palabra] = diccionario[palabra] + 1
    else:
      diccionario[palabra] = 1
  return diccionario

print(contadorDePalabras("Hola que tal. Que pensas hacer hoy que esta lluvioso?"))