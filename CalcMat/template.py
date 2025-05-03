#!/usr/bin/env python3


"""
Título de práctica: Ejercicio CalcMat

Descripción extendida del programa

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha: 2025-05-02
"""


class Matriz:
    def __init__(self, elementos):
        self.valores = elementos

    def __add__(self, otra):
        resultado = [
            [self.valores[i][j] + otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __sub__(self, otra):
        resultado = [
            [self.valores[i][j] - otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __mul__(self, otra):
        resultado = [
            [
                self.valores[i][0] * otra.valores[0][j] +
                self.valores[i][1] * otra.valores[1][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Matriz(resultado)

    def mostrar(self, nombre=""):
        if nombre:
            print(f"> {nombre}:")
        for fila in self.valores:
            print(f"> |{fila[0]}  {fila[1]}|")


def leer_matriz(numero):
    valores = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"> Matriz {numero}: elemento {i},{j}\n< "))
            fila.append(valor)
        valores.append(fila)
    return Matriz(valores)


def main():
    matriz1 = leer_matriz(1)
    matriz2 = leer_matriz(2)

    matriz1.mostrar("Matriz 1")
    matriz2.mostrar("Matriz 2")

    print("> Escriba 1 para suma, ")
    print(">         2 para resta, ")
    print(">         3 para multiplicación ")
    opcion = input("< ")

    if opcion == "1":
        resultado = matriz1 + matriz2
        print("> La suma de las dos matrices es:")
        resultado.mostrar()
    elif opcion == "2":
        resultado = matriz1 - matriz2
        print("> La resta de las dos matrices es:")
        resultado.mostrar()
    elif opcion == "3":
        resultado = matriz1 * matriz2
        print("> La multiplicación de las dos matrices es:")
        resultado.mostrar()
    else:
        print("> Opción inválida.")


"""
para usar pycodestyle ejecutar el comando
python -m pycodestyle --first CalcMat\template.py
"""

if __name__ == "__main__":
    main()
