"""
Realiza un programa que reciba una cantidad de minutos y  
muestre por pantalla a cuantas horas y minutos corresponde
Entrada:
   minutos: int
Salida:
   minutos y Horas correspondientes
"""
minutos = input("Ingresa los minutos: ")
minutos = int(minutos)
hora = minutos/60
minutosres = minutos % 60
print("Las horas son : ",hora , minutosres)