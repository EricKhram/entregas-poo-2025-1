#!/usr/bin/env python3
import datetime


"""
Título de práctica: Ejercicio Mascotas1

Descripción extendida del programa

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha: 2025-03-29
"""


class Mascotas:
    """creacion de la clase"""
    def __init__(self, clase, nombre, raza, edad, ingreso):
        self.clase = clase
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.ingreso = ingreso

    """Devuelve los datos de la mascota en forma de lista"""
    def obtener_datos(self):
        return [self.nombre,
                self.clase,
                f"{self.raza}",
                f"{self.edad} años",
                f"{self.ingreso}"]


"""funcion para que el usuario ingrese su mascota"""


def ingresar_mascota():
    clase = input("es perro o gato?: ").lower()
    nombre = input(f"Ingrese el nombre de su {clase}: ")
    raza = input(f"Cual es la raza de '{nombre}'?: ")
    edad = int(input(f"Que edad en años tiene '{nombre}': "))
    # asignamos a una variable la fecha y hora de ingreso actual
    ingres = datetime.datetime.now()
    # quitamos los microsegundos de la hora de ingreso
    ingreso = ingres.replace(microsecond=0)
    return Mascotas(clase, nombre, raza, edad, ingreso)


"""funcion para imprimir las mascotas ingresadas en forma de tabla"""


def mostrar_mascotas(mascotas):
    # Encabezados de la tabla
    headers = ["clase", "nombre", "raza", "edad", "fecha de ingreso"]
    # Imprimimos la cabecera de la tabla
    print(f"{headers[0]:<15} {headers[1]:<20}"
          f"{headers[2]:<15} {headers[3]:<15}"
          f"{headers[4]:<20}")
    # Mostramos los productos con formato de tabla
    for mascota_obj in mascotas:
        clase, nombre, raza, edad, ingreso = mascota_obj.obtener_datos()
        print(f"{clase:<15} {nombre:<20} {raza:<15} {edad:<15} {ingreso:<20}")


def main():
    mascotas = []
    nmascotas = int(input("cuantas mascotas desea ingresar: "))
    # Pedimos los datos para las mascotas
    for i in range(nmascotas):
        print(f"\nmascota {i+1}:")
        mascota_obj = ingresar_mascota()
        mascotas.append(mascota_obj)
    # Mostramos los productos ingresados en formato de tabla
    print("\nDatos de las mascotas ingresadas:")
    mostrar_mascotas(mascotas)


"""
para usar pycodestyle ejecutar el comando
python -m pycodestyle --first Mascotas1\template.py
"""


# Llamamos a la función principal
if __name__ == "__main__":
    main()
