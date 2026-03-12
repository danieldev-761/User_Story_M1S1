while True:    
    print("------------------------------------------")
    print("-------- Registro de ventas --------------")
    print("------------------------------------------")

    while True:
        nombres = input("Nombre del cliente: ").strip().capitalize()
        if nombres == "":
            print("El nombre no puede estar vacío.")
        elif nombres.isnumeric():
            print("El nombre no puede ser solo números.")
        else:
            break

    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: Debes ingresar un número válido para el precio.")

    # Validar cantidad (solo enteros)
    while True:
        try:
            cantidad_compra = int(input("Ingresa la cantidad comprada: "))
            if cantidad_compra <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
    



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