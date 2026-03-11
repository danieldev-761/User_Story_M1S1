# costo total

precio= float(input("ingrese el precio del producto: "))
cantidad= int(input("ingrese la cantidad del producto: "))

#validacion 
if precio >= 0 and cantidad >= 0:
    costo_total= precio * cantidad
    print("el costo total es: ", costo_total)
else:
    print("error precio o cantidad invalida")

# resultado
print("----resultado inventario----")
print("precio: ", precio)
print("cantidad: ", cantidad)
print("costo total: ", costo_total)