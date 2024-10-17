"""
 Un alumno desea saber cuál será su calificación final en la materia de 
Algoritmos Dicha calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
Entrada:
  parcial1:int
  parcial2:int
  parcial3:int
  examen final:int
  trabajo final:int
Salida:
  calificacion final
"""
parcial1 = input("Ingresa la calificacion de el primer parcial: ")
parcial1 = int(parcial1)
parcial2 = input("Ingresa la calificacion de el segundo parcial: ")
parcial2 = int(parcial2)
parcial3 = input("Ingresa la calificacion de el tercer parcial: ")
parcial3 = int(parcial3)
examFinal = input("Ingresa la calificacion de el examen final: ")
examFinal = int(examFinal)
trabFinal = input("Ingresa la calificacion de el trabajo final: ")
trabFinal = int(examFinal)
parciales = parcial1 + parcial2 + parcial3
promedio = parciales/3
calFinal = promedio * 0.55 + examFinal * 0.3 + trabFinal * 0.15
print("La Calificacion final es: ", calFinal)