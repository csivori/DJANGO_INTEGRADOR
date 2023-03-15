import ejercicio3 

def obtenerLaPalabraMasFrecuente(diccionarioPalabrasContadas:dict)->tuple:
  '''Dado un diccionario de las Palabras Contadas, devuelve una tupla con la palabra con mas apariciones'''
  maximo = 0
  for palabra in diccionarioPalabrasContadas:
    if diccionarioPalabrasContadas[palabra] > maximo:
      palabraMasFrecuente = palabra
      maximo = diccionarioPalabrasContadas[palabra]
  return (palabraMasFrecuente, diccionarioPalabrasContadas[palabraMasFrecuente])

print(obtenerLaPalabraMasFrecuente(ejercicio3.contadorDePalabras("Hola que tal. Que pensas hacer hoy que esta lluvioso?")))