"""
 Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su 
raíz cúbica.
¿cómo se puede calcular?
Entrada:
  numero:int
Salida:
  raiz cuadrada
  raiz cubica
"""
num1 = input("Ingresa un numero: ")
num1 = int(num1)
raizCuadrada = num1 ** (1/2)
raizCubica = num1 ** (1/3)
print("La raiz cuadrada es: ", raizCuadrada )
print("La raiz cubica es: ", raizCubica)