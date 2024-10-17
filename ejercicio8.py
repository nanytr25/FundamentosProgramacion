"""
 Un vendedor recibe un sueldo base más un 10% extra por comisión de sus 
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de 
comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes 
tomando en cuenta su sueldo base y comisiones
Entrada:
  sueldo:int
  venta1:int
  venta2:int
  venta3:int
Salida:
sueldo total
"""
venta1 = input("Ingresa el total de la primer venta: ")
venta1 = int(venta1)
venta2 = input("Ingresa el total de la segunda venta: ")
venta2 = int(venta2)
venta3 = input("Ingresa el total de la tercer venta: ")
venta3 = int(venta3)
sueldo = input("Ingresa el sueldo base: ")
sueldo = int(sueldo)
ventaTotal = venta1 + venta2 + venta3
comision = ventaTotal * 0.1
sueldoTotal = sueldo + comision
print ("El sueldo total es de: ", sueldoTotal)