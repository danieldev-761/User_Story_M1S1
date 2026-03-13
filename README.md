# Inventario Simple

Este repositorio contiene un programa en Python llamado `inventario.py` que permite al usuario:

1. Registrar productos ingresando nombre, precio y cantidad.
2. Calcular el total de unidades registradas.
3. Estimar el costo total del inventario.
4. Ejecutar varias entradas de datos en un bucle opcional.

El código es intencionalmente sencillo y está pensado como un ejercicio de fundamentos de programación que incluye:

- Lectura de datos desde la consola
- Uso de variables y tipos básicos
- Operaciones aritméticas
- Salida de resultados por pantalla

## Uso

Para ejecutar el programa siga estos pasos:

1. Abra una terminal y navegue hasta el directorio del proyecto.
2. Asegúrese de tener Python 3 instalado (`python3 --version`).
3. Ejecute el script con el siguiente comando:

   ```bash
   python3 inventario.py
   ```

4. Cuando aparezca el mensaje de registro, ingrese el nombre del producto, el precio y la cantidad.
5. El programa mostrará el costo total y el resumen del inventario.
6. Cuando se le pregunte si desea registrar otra venta, ingrese `1` para continuar o cualquier otra tecla para finalizar.

El resto del funcionamiento se realiza siguiendo las indicaciones en pantalla.
### Ejemplo de ejecución/salida

```
------------------------------------------
-------- Registro de ventas --------------
------------------------------------------
Nombre del producto: Pan
Precio del producto: 500
Ingresa la cantidad comprada: 5
el costo total es:  2500.0
----Resultado Inventario----
Producto: Pan | Precio: 500.0 | Cantidad: 5 |Costo total: 2500.0
¿Deseas registrar otra venta? (1 para sí, cualquier otra tecla para no): 0
```

## Miembros del equipo

- Isaac Ortiz
- Daniel Echeverría
- Luis Fuentes

## Licencia

Este proyecto se distribuye bajo la Licencia Pública General GNU (GPL). Consulta el archivo `LICENSE` para más detalles.
