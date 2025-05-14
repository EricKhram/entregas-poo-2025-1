#!/usr/bin/env python3


"""
Título de práctica: Ejercicio GUIHello con TkInder

Descripción extendida del programa

Autor: Erick Lopez
<eslopezf@academia.usbbog.edu.co>
Fecha: 2025-05-13
"""

import tkinter as tk
from tkinter import messagebox


class VentanaSaludo:
    def __init__(self, ventana):
        # Guardamos la confguracion de la ventana
        self.ventana = ventana
        self.ventana.title("Ventana de saludo")
        self.ventana.geometry("300x200")
        self.ventana.configure(bg="#009bab")

        # Crea los objetos dentro de la ventana
        self.crear_widgets()

    def crear_widgets(self):
        # Label
        self.label_nombre = tk.Label(
            self.ventana, text="¿Como te llamas?:",
            bg="#009bab", fg="white", font=("Arial", 12)
        )
        self.label_nombre.pack(pady=10)

        # Entrada
        self.entry_nombre = tk.Entry(self.ventana, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)

        # Botón de saludo
        self.boton_saludar = tk.Button(
            self.ventana, text="Saludar",
            command=self.saludar, bg="#4CAF50",
            fg="white", font=("Arial", 11)
        )
        self.boton_saludar.pack(pady=10)

        # Botón de salir
        self.boton_salir = tk.Button(
            self.ventana, text="Salir",
            command=self.ventana.quit, bg="#f44336",
            fg="white", font=("Arial", 11)
        )
        self.boton_salir.pack()

    def saludar(self):
        nombre = self.entry_nombre.get()
        if nombre.strip() == "":
            messagebox.showwarning(
                "Advertencia", "Por favor ingrese un nombre.")
        else:
            messagebox.showinfo("Saludo", f"Hola {nombre}")


"""
para usar pycodestyle ejecutar el comando
python -m pycodestyle --first GUIHello\template.py
"""

ventana = tk.Tk()
app = VentanaSaludo(ventana)
ventana.mainloop()
