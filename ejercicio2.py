"""
Programa 2:
    Crea un programa que calcule area y perimetro
    de un rectangulo
Entradas:
    Base: integer
    altuea: integer 
Salidas:
    area: integer
    perimetro: integer        
"""
base = input("Ingresa la base: ")
base = int(base)
altura = input("Ingresa la altura: ")
altura = int(altura)
area = base * altura
perimetro = (base + altura) * 2
print ("El area de el rectangulo es: ", area)
print ("El perimetro de el rectangulo es: ", perimetro)