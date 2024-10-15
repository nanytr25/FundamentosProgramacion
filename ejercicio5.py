"""
Programa que convierta un valor dado en grados farenheit
a grados celsius
Entrada:
  grados Fahrenheit: int
salida:
  grados Celsius  
"""
gradosFare = input("Ingresa los grados Fahrenheit:" )
gradosFare = int(gradosFare)
celsius = gradosFare - 32
celsius = celsius * 5/9
print("La conversion de Fahrenheit a Celsius es de: ",celsius)