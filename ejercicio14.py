"""
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el 
número invertido
Entrada:
   numero:int
Salida:
   numero invertido
"""
num = input("Ingresa un numero de dos cifras: ")
num = int(num)
dec = num // 10
uni = num % 10
print("El numero invertido es:" , uni,dec)