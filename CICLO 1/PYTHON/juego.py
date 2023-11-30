import random

class AdivinarNumero:
  """
  Juega al juego de adivinar el número.

  Args:
    nombre: El nombre del jugador.

  Returns:
    El número de intentos que hizo el jugador para adivinar el número.
  """

  def __init__(self, nombre):
    self.nombre = nombre
    self.numero_secreto = random.randint(1, 1000)
    self.intentos = 1

  def jugar(self):
    while self.intentos <= 10:
      print(f"Intentos: {self.intentos}/{10}")
      numero_ingresado = input("Ingrese un número: ")

      if int(numero_ingresado) == self.numero_secreto:
        return self.intentos

      if int(numero_ingresado) < self.numero_secreto:
        print("¡El número es mayor!")
      else:
        print("¡El número es menor!")

      self.intentos += 1

    return self.intentos

def main():
  nombre = input("¿Cuál es tu nombre? ")
  juego = AdivinarNumero(nombre)
  numero_de_intentos = juego.jugar()

  if numero_de_intentos <= 10:
    print(f"¡Felicidades, {nombre}! Ganaste con {numero_de_intentos} intentos.")
  else:
    print(f"¡Lo siento, {nombre}! No pudiste adivinar el número en 10 intentos.")

if __name__ == "__main__":
  main()
