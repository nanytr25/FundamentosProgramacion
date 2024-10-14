"""
Programa que calcule la hipotenusa de un triangulo 
rectangulo a partir de sus catetos
Entradas: 
   cateto1: int
   cateto2: int
Salidas:
   hipotenusa
Analisis:
   Se resuelve con el teorema de pitagoras    
"""
cateto1 = input("Ingresa el cateto1: ")
cateto1 = int (cateto1)
cateto2 = int (input("Ingresa el cateto2: "))
hipotenusa = cateto1 * cateto1 + cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)
print("La hipotenusa es: ", hipotenusa)