import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import customtkinter
import os
from PIL import Image
import json
import os
from datetime import datetime

# Tema y colores

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Usuarios")
        self.geometry("400x400")
        self.resizable(False,False)

        self.lista_usuarios_boton = customtkinter.CTkButton(self, text="Lista de usuarios", command=self.lista_usuarios)
        self.lista_usuarios_boton.pack(pady=10)


    def lista_usuarios(self):
        # Crear una nueva ventana
        top = customtkinter.CTkToplevel(self)
        top.title("Lista de usuarios")
        top.geometry("800x600")
        top.resizable(False,False)

        # Crear un frame
        frame = customtkinter.CTkFrame(top, corner_radius=10)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear un treeview
        treeview = customtkinter.CTkTreeview(frame, columns=("Nom", "Cognom", "DNI", "Correu", "Telefon"), show="headings")
        treeview.pack(pady=20, padx=20, fill="both" , expand=True)

        treeview.heading("Nom", text="Nom")
        treeview.heading("Cognom", text="Cognom")
        treeview.heading("DNI", text="DNI")
        treeview.heading("Correu", text="Correu")
        treeview.heading("Telefon", text="Telefon")

        treeview.column("Nom", width=100)
        treeview.column("Cognom", width=100)
        treeview.column("DNI", width=100)
        treeview.column("Correu", width=100)
        treeview.column("Telefon", width=100)

        for dni, info in self.usuarios.items():
            treeview.insert("", "end", values=(dni, info["nombre"], info["apellido"], info["correo"], info["telefono"]))

    def cargar_datos(self):
        """Carga los datos de los archivos de texto al iniciar el programa."""
        if os.path.exists("data/usuarios.txt"):
            with open("data/usuarios.txt", "r") as file:
                self.usuarios = json.load(file)

if __name__ == "__main__":
    app = App()
    app.mainloop()  # Iniciar la aplicación