print("""
---------------Registro de ventas--------------
        1. Nuevo producto 
        2. Salir

""")
opcion = input("Que opcion deseas realizar? ")

while True:
        if opcion == "1":
                        nombres = input("Nombre del producto: ").strip().capitalize()
                        if nombres == "" or nombres.isnumeric():
                                print("El nombre no puede estar vacío o no puede ser solo números..")

                        else:
                                try:
                                        precio =float(input("Digite el precio del producto: "))
                                        
                                        if precio < 0 :
                                                print("El valor no puede ser menor a 0 o por de bajo de 0 ")
                                                continue

                                        cantidad = int(input("Ingrese la cantidad del producto: "))

                                        if cantidad > 0:
                                                print("La cantidad no puede ser menor a 0 o 0")
                                except ValueError:
                                        print("ERROR: No se acepta ese tipo de valor")





