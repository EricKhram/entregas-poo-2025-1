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
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def obtener_datos(self):
        # Devuelve los datos del producto en forma de lista
        return [self.nombre,
                f"${self.precio:.2f} COP",
                f"{self.cantidad} unidades"]


def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Cual es el precio de '{nombre}'?: "))
    cantidad = int(input(f"Que cantidad hay de '{nombre}': "))
    return Producto(nombre, precio, cantidad)


def mostrar_productos(productos):
    # Encabezados de la tabla
    headers = ["Nombre", "Precio", "Cantidad"]
    # Imprimimos la cabecera de la tabla
    print(f"{headers[0]:<15} {headers[1]:<20} {headers[2]:<15}")
    # Mostramos los productos con formato de tabla
    for producto in productos:
        nombre, precio, cantidad = producto.obtener_datos()
        print(f"{nombre:<15} {precio:<20} {cantidad:<15}")


def main():
    productos = []
    # Pedimos los datos para tres productos
    for i in range(3):
        print(f"\nProducto {i+1}:")
        producto = ingresar_producto()
        productos.append(producto)
    # Mostramos los productos ingresados en formato de tabla
    print("\nDatos de los productos ingresados:")
    mostrar_productos(productos)


"""
para usar pycodestyle ejecutar el comando
pycodestyle --first Tienda1\template.py
"""
# Llamamos a la función principal
if __name__ == "__main__":
    main()
