"""
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos 
puntos en el plano. Calcula y muestra la distancia entre ellos
Entrada:
  x1:int
  y1:int
  x2:int
  y2:int
Salida:
  distancia
"""
num1x = input("Ingresa el primer numero x: ")
num1x = int(num1x)
num1y = input("Ingresa el primer numero y: ")
num1y = int(num1y)
num2x = input("Ingresa el segundo numero x: ")
num2x = int(num2x)
num2y = input("Ingresa el segundo numero y: ")
num2y = int(num2y)
distancia = num1x + num1y * num1x + num1y + num2x + num2y * num2x + num2y
resultado = distancia ** (1/2)
print("La distancia es de:", resultado)