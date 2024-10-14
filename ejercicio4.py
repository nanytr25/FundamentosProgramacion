"""
Dado los numeros, mostrar la suma, resta, division
y multiplicacion
Entrada:
   num1: int
   num2: int
salida: 
   suma
   resta
   division
   multiplicacion   
"""
num1 = input("Ingresa el primer numero: ")
num1 = int(num1)
num2 = input("Ingresa el segundo numero: ")
num2 = int(num2)
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multiplicacion)
print("La division es: ", division)