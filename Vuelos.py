# Diccionario de vuelos
vuelos = {
    "AV101": {"destino": "Bogota", "asientos": 5, "precio": 300},
    "AV202": {"destino": "Medellin", "asientos": 3, "precio": 200},
    "AV303": {"destino": "Cartagena", "asientos": 4, "precio": 250},
    "AV404": {"destino": "Cali", "asientos": 2, "precio": 220}
}

# Lista para guardar reservas
reservas = []

# Variable para el dinero total
total_dinero = 0

while True:

    print("\nVuelos disponibles:")
    for codigo, datos in vuelos.items():
        print(codigo, "-", datos["destino"], "- Asientos:", datos["asientos"], "- Precio:", datos["precio"])

    # Pedir nombre
    nombre = input("\nNombre del pasajero (o escriba 'salir'): ")

    if nombre.lower() == "salir":
        break

    # Pedir datos de reserva
    codigo_vuelo = input("Codigo de vuelo: ")
    cantidad = int(input("Cantidad de asientos: "))

    # Validar si el vuelo existe
    if codigo_vuelo in vuelos:

        # Validar asientos disponibles
        if vuelos[codigo_vuelo]["asientos"] >= cantidad:

            # Guardar reserva
            reserva = {
                "nombre": nombre,
                "codigo": codigo_vuelo,
                "cantidad": cantidad
            }

            reservas.append(reserva)

            # Descontar asientos
            vuelos[codigo_vuelo]["asientos"] -= cantidad

            # Calcular dinero
            total_dinero += vuelos[codigo_vuelo]["precio"] * cantidad

            print("Reserva realizada con éxito")

        else:
            print("No hay suficientes asientos disponibles")

    else:
        print("El vuelo no existe")


# Mostrar resultados finales
print("\nReservas realizadas:")
conteo_vuelos = {}

for r in reservas:
    print(r["nombre"], "-", r["codigo"], "-", r["cantidad"], "asientos")

    if r["codigo"] in conteo_vuelos:
        conteo_vuelos[r["codigo"]] += 1
    else:
        conteo_vuelos[r["codigo"]] = 1


print("\nDinero total recaudado:", total_dinero)

# Vuelo con más reservas
if conteo_vuelos:
    vuelo_mas_reservas = max(conteo_vuelos, key=conteo_vuelos.get)
    print("Vuelo con más reservas:", vuelo_mas_reservas)
else:
    print("No se realizaron reservas.")