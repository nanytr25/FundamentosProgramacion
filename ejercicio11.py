"""
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor 
absoluto de su diferencia, de modo que el resultado sea siempre positivo)
Entrada:
  num1:int
  num2:int 
Salida:
  distancia
"""
num1 = input("Ingresa el primer numero: ")
num1 = int(num1)
num2 = input("Ingresa el segundo numero: ")
num2 = int(num2)
distancia = num1 - num2
x = abs(distancia)
print("La distancia es de:", x)