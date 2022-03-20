listaColor=["rojo","verde","amarillo","negro","blanco"]
listaTipo=["gasolina","electrico"]
class Asiento:
  def __init__(self,color,precio,registro):
    self.color=color
    self.precio=precio
    self.registro=registro
  def cambiarColor(self,color):
    if color in listaColor:
      self.color=color
class Auto:
  cantidadCreados=0
  def __init__(self,modelo,precio,asientos,marca,motor,registro):
    self.modelo=modelo
    self.precio=precio
    self.asientos=asientos
    self.marca=marca
    self.motor=motor
    self.registro=registro
  def cantidadAsientos(self):
    c=0
    for asiento in self.asientos:
      if type(asiento).__name__=="Asiento":
        c+=1
    return c
  def verificarIntegridad(self):
    if self.registro==self.motor.registro:
      for a in self.asientos:
        if type(a).__name__=="Asiento":
          if a.registro!=self.registro:
            return "Las piezas no son originales"
      return "Auto original"  
    return "Las piezas no son originales"
class Motor:
  def __init__(self,numeroCilindros,tipo,registro):
    self.numeroCilindros=numeroCilindros
    self.tipo=tipo
    self.registro=registro
  def cambiarRegistro(self,registro):
    self.registro=registro
  def asignarTipo(self,tipo):
    if tipo in listaTipo:
      self.tipo=tipo
    
    
    
      
    
    