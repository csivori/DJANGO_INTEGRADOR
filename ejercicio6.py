class Persona():
  """
  Modela una Persona.
  
  Atributos:
   - nombre:Persona
   - edad:int
   - dni:int
    
  Métodos:
   - mostrar(): Muestra los datos de la persona. 
   - EsMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
  """

  def __init__(self, nombre:str=None, edad:int=None, dni:int=None) -> None:
    self.nombre = nombre
    self.edad = edad
    self.dni = dni

  def __str__(self) -> str:
    return f"Persona (Nombre:{self.nombre}, Edad:{self.edad}, DNI:{self.dni})"
# 
# Getters & Setters
# 
  def getNombre(self) -> str:
    return self.nombre

  def getEdad(self) -> int:
    return self.edad

  def getDni(self) -> int:
    return self.dni
  
  def setNombre(self, nombre:str) -> None:
    if len(nombre) > 1:
      self.nombre = nombre
    else:
      raise Exception("El Nombre debe tener al menos 2 letras")

  def setEdad(self, edad:int) -> None:
    if edad >= 0 and edad <= 200:
      self.edad = edad
    else:
      raise Exception("La Edad debe estar entre 0 y 200")

  def setDni(self, dni:int) -> None:
    if dni >= 1000000 and dni < 100000000:
      self.dni = dni
    else:
      raise Exception("El DNI debe ser Mayor a 1.000.000 y menor a 100.000.000")
# 
# Métodos Públicos
# 
  def mostrar(self) -> None:
    '''Muestra x consola los datos de la Persona'''
    print(self)

  def esMayorDeEdad(self) -> bool:
    '''Devuelve True/False indicando si es mayor de edad'''
    if self.edad == None:
      raise Exception("Esta Persona no tiene la edad definida aún")
    return self.edad >= 21
# 
# Métodos Privados
# 
