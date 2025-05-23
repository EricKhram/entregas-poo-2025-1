#!/usr/bin/env python3
import datetime

"""
Título de práctica: Mascotas2

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha de modificación: 2025-04-26
"""



class Visualizador:
    def resumen(self):
        datos = self.mostrar_datos()
        print(
            f"{datos[0]:<8} {datos[1]:<12}"
            f"{datos[2]:<8} {datos[3]:<20}"
            f"{datos[4]:<20}"
        )


class Mascota(Visualizador):
    """Mascotas que ingresan a una veterinaria"""
    def __init__(self, Nombre, Edad, Raza):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Raza = Raza
        self.FechaIN = datetime.now().isoformat()

    def mostrar_datos(self):
        return [
            self.__class__.clase,
            self.Nombre,
            f'{self.Edad} años',
            self.Raza,
            self.FechaIN,
        ]


class Perro(Mascota):
    clase = "perro"


class Gato(Mascota):
    clase = "gato"


def info_mascotas():
    """Agrega una mascota"""
    mascotas = []
    cantidad = int(input("¿Cuantas mascotas vas a ingresar? "))
    for i in range(1, cantidad + 1):
        TipoMascota = input(f"Mascota {i}, "
                            "¿Es perro o gato?").strip().lower()
        while TipoMascota not in ['perro', 'gato']:
            TipoMascota = input("Opcion no valida, "
                                "ingrese, que tipo de mascota "
                                f"es Mascota {i}, ¿Es perro o gato? ")
        Nombre = input(f"¿Cúal es el nombre del {TipoMascota}?: ")
        Edad = int(input(f"¿Que edad tiene {Nombre}?: "))
        Raza = input(f"Que raza es {Nombre}?: ")
        mascota = (
            Perro(Nombre, Edad, Raza) if TipoMascota == 'perro'
            else Gato(Nombre, Edad, Raza))
        mascotas.append(mascota)
    return mascotas


def Mostrar(mascotas):
    """Muestra las mascotas ingresadas"""
    encabezado = ["Clase", "Nombre", "Edad", "Raza", "Fecha ingreso"]
    print(
        f"{encabezado[0]:<8} {encabezado[1]:<12}"
        f"{encabezado[2]:<8} {encabezado[3]:<20}"
        f"{encabezado[4]:<20}"
    )
    for mascota in mascotas:
        mascota.resumen()

"""
para usar pycodestyle ejecutar el comando
python -m pycodestyle --first Mascotas1\template.py
"""


if __name__ == "__main__":
    mascotas = info_mascotas()
    Mostrar(mascotas)