#!/usr/bin/env python3

"""
Título de práctica: Ejercicio Tienda1

Descripción extendida del programa

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha: 2025-02-27
"""


class Producto:
    """creacion de la clase"""
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def obtener_datos(self):
        # Devuelve los datos del producto en forma de lista
        return [self.nombre,
                f"${self.precio:.2f} COP",
                f"{self.cantidad} unidades",
                f"{self.descripcion}",
                f"{self.clasificacion}"]


def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Cual es el precio de '{nombre}'?: "))
    cantidad = int(input(f"Que cantidad hay de '{nombre}': "))
    descripcion = input(f"introduzca la descripcion de '{nombre}': ")
    clasificacion = input(f"Que clasificacion tiene '{nombre}': ")
    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def mostrar_productos(productos):
    # Encabezados de la tabla
    headers = ["Nombre", "Precio", "Cantidad", "descripcion", "clasificacion"]
    # Imprimimos la cabecera de la tabla
    print("\nDatos de los productos ingresados:")
    print(f"{headers[0]:<15} {headers[1]:<20} {headers[2]:<15} {headers[3]:<20} {headers[4]:<30}")
    # Mostramos los productos con formato de tabla
    for producto in productos:
        nombre, precio, cantidad, descripcion, clasificacion = producto.obtener_datos()
        print(f"{nombre:<15} {precio:<20} {cantidad:<15} {descripcion:<20} {clasificacion:<30}")


def mostrar_productos_agrupados(productos):
    # Diccionario para almacenar la suma de precios por clasificación
    clasificaciones = {}
    for producto in productos:
        if producto.clasificacion in clasificaciones:
            clasificaciones[producto.clasificacion] += producto.precio
        else:
            clasificaciones[producto.clasificacion] = producto.precio
    print("\nSuma de precios por clasificación:")
    print(f"{'Clasificación':<20} {'Precio Total':<15}")
    for clasificacion, precio_total in clasificaciones.items():
        print(f"{clasificacion:<20} ${precio_total:.2f} COP")


def main():
    nproductos = int(input("cuantos productos va a ingresar?: "))
    # pedimos el numero de productos que ingresara el usuario
    productos = []
    # Pedimos los datos para n productos
    for i in range(nproductos):
        print(f"\nProducto {i+1}:")
        producto = ingresar_producto()
        productos.append(producto)
    # Mostramos los productos ingresados en formato de tabla
    mostrar_productos(productos)
    mostrar_productos_agrupados(productos)


"""
para usar pycodestyle ejecutar el comando
pycodestyle --first template.py
"""
# Llamamos a la función principal
if __name__ == "__main__":
    main()
