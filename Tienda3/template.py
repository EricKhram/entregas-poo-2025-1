#!/usr/bin/env python3

"""
Título de práctica: Ejercicio Tienda3

Descripción extendida del programa

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha: 2025-03-17
"""

class Producto:
    """creacion de la clase"""
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion, tti, pcu):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.tti = tti
        self.pcu = pcu
        
    def obtener_datos(self):
        # Devuelve los datos del producto en forma de lista
        return [self.nombre,
                f"${self.precio:.2f} COP",
                f"{self.cantidad} unidades",
                f"{self.descripcion}",
                f"{self.clasificacion}",
                f"{self.tti:.2f} COP",
                f"{self.pcu:.2f} COP"]
        

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Cual es el precio de '{nombre}'?: "))
    cantidad = int(input(f"Que cantidad hay de '{nombre}': "))
    descripcion = input(f"introduzca la descripcion de '{nombre}': ")
    clasificacion = input(f"Que clasificacion tiene '{nombre}': ").lower()
    tti = precio * cantidad
    pcu = precio * 5
    return Producto(nombre, precio, cantidad, descripcion, clasificacion, tti, pcu)


def mostrar_productos(productos):
    # Encabezados de la tabla
    headers = ["Nombre", "Precio", "Cantidad", "descripcion", "clasificacion", "total en inventario", "preciox5"]
    # Imprimimos la cabecera de la tabla
    print("\nDatos de los productos ingresados:")
    print(
        f"{headers[0]:<15} {headers[1]:<20} {headers[2]:<15}"
        f"{headers[3]:<30} {headers[4]:<18} {headers[5]:<20} {headers[6]}")
    #linea divisoria entre encabezados de la tabla y contenidos
    print("---------------------------------------------------------------"
            "-------------------------------------------------------------------")
    # Mostramos los productos con formato de tabla
    for producto in productos:
        (
            nombre, precio, cantidad,
            descripcion, clasificacion, tti, pcu
        ) = producto.obtener_datos()
        print(
            f"{nombre:<15} {precio:<20} {cantidad:<15}"
            f"{descripcion:<30} {clasificacion:<18} {tti:<20} {pcu}")
        

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


# Llamamos a la función principal
if __name__ == "__main__":
    main()
    
