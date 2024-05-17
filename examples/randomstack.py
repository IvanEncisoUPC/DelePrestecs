import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Inicializar la aplicación CustomTkinter
ctk.set_appearance_mode("System")  # Modos: "System" (según el SO), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.title("Pantalla Principal")
        self.geometry("400x300")

        # Crear un botón que abre la ventana con el Treeview
        open_button = ctk.CTkButton(self, text="Abrir Tabla", command=self.open_table_window)
        open_button.pack(pady=50)

    def open_table_window(self):
        # Crear una nueva ventana Toplevel
        top = ctk.CTkToplevel(self)
        top.title("Tabla en Toplevel")
        top.geometry("600x400")

        # Crear un frame de CustomTkinter dentro del Toplevel
        frame = ctk.CTkFrame(top, corner_radius=10)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear un Treeview dentro del frame
        treeview = ttk.Treeview(frame, columns=("A", "B", "C"), show="headings", height=10)
        treeview.pack(pady=20, padx=20, fill="both", expand=True)

        # Definir los encabezados de columna
        treeview.heading("A", text="Columna A")
        treeview.heading("B", text="Columna B")
        treeview.heading("C", text="Columna C")

        # Definir el tamaño de las columnas
        treeview.column("A", width=100)
        treeview.column("B", width=100)
        treeview.column("C", width=100)

        # Agregar algunos datos
        data = [
            ("Item 1A", "Item 1B", "Item 1C"),
            ("Item 2A", "Item 2B", "Item 2C"),
            ("Item 3A", "Item 3B", "Item 3C")
        ]

        for item in data:
            treeview.insert("", tk.END, values=item)

if __name__ == "__main__":
    app = App()
    app.mainloop()
