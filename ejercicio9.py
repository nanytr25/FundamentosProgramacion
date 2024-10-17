"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuánto deberá pagar finalmente por su compra.
Entrada:
  total de la compra: int
Salida:
  Total a pagar
"""
totalCompra = input("Ingresa el Total de la compra: ")
totalCompra = int(totalCompra)
descuento = totalCompra * 15
descuento = descuento / 100
total = totalCompra - descuento
print ("El total a apagar aplicando el descuento es: ", total)