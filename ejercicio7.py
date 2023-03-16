from ejercicio6 import Persona

class Cuenta():
  '''
  Simula una Cuenta Bancaria.
  
  Atributos:
   - titular:Persona
   - cantidad:float
    
  Métodos:
   - mostrar(): Muestra los datos de la cuenta. 
   - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
   - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
  '''

  def __init__(self, titular:Persona=None, cantidad:float=0.0) -> None:
    self.titular = titular
    self.cantidad = cantidad

  def __str__(self) -> str:
    return f"Cuenta (Titular:{self.titular}, Cantidad:{self.cantidad})"
# 
# Getters & Setters
# 
  def getTitular(self) -> Persona:
    return self.titular

  def getCantidad(self) -> float:
    return self.cantidad
  
  def setTitular(self, titular:Persona) -> None:
    if titular != None:
      self.titular = titular
    else:
      raise Exception("El Titular no puede ser Nulo")

  def setCantidad(self, cantidad:float) -> None:
    if cantidad != None:
      self.cantidad = cantidad
    else:
      raise Exception("La Cantidad no puede ser Nula")
# 
# Métodos Públicos
# 
  def mostrar(self) -> None:
    '''Muestra x consola los datos de la Cuenta'''

    print(self)

  def ingresar(self, cantidad:float) -> None:
    '''Ingresa la cantidad a la cuenta. Si la cantidad introducida es negativa, no se hará nada.'''

    if cantidad != None:
      if cantidad > 0:
        self.cantidad += cantidad
      elif cantidad < 0:
        raise Exception("La Cantidad no puede ser Negativa")
    else:
      raise Exception("La Cantidad no puede ser Nula")

  def retirar(self, cantidad:float) -> None:
    '''Retira la cantidad de la cuenta, pudiendo quedar en negativo.'''

    if cantidad != None:
      if cantidad > 0:
        self.cantidad -= cantidad
      elif cantidad < 0:
        raise Exception("La Cantidad no puede ser Negativa")
    else:
      raise Exception("La Cantidad no puede ser Nula")
# 
# Métodos Privados
# 
