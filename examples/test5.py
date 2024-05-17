import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime
import json
import os

class PrestamoMaterial:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Préstamo de Material")

        self.usuarios = {}
        self.materiales = {f"bata{i:02d}": True for i in range(1, 6)}
        self.materiales.update({f"gafas{i:02d}": True for i in range(1, 6)})
        self.materiales.update({f"calculadora{i:02d}": True for i in range(1, 6)})
        self.prestamos = []

        self.cargar_datos()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.button_add_user = tk.Button(self.frame, text="Añadir Usuario", command=self.registrar_usuario)
        self.button_add_user.grid(row=0, column=0, pady=5)

        self.button_view_users = tk.Button(self.frame, text="Ver Usuarios Verificados", command=self.ver_usuarios)
        self.button_view_users.grid(row=1, column=0, pady=5)

        self.button_view_materials = tk.Button(self.frame, text="Ver Materiales Disponibles", command=self.ver_materiales)
        self.button_view_materials.grid(row=2, column=0, pady=5)

        self.button_new_loan = tk.Button(self.frame, text="Nuevo Préstamo", command=self.nuevo_prestamo)
        self.button_new_loan.grid(row=3, column=0, pady=5)

        self.button_return_material = tk.Button(self.frame, text="Devolver Material", command=self.devolver_material)
        self.button_return_material.grid(row=4, column=0, pady=5)

        self.button_view_loans = tk.Button(self.frame, text="Ver Préstamos Actuales", command=self.ver_prestamos)
        self.button_view_loans.grid(row=5, column=0, pady=5)

        # Configurar el evento para guardar datos al cerrar la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.guardar_datos)

    def cargar_datos(self):
        """Carga los datos de los archivos de texto al iniciar el programa."""
        if os.path.exists("usuarios.txt"):
            with open("usuarios.txt", "r") as file:
                self.usuarios = json.load(file)

        if os.path.exists("materiales.txt"):
            with open("materiales.txt", "r") as file:
                self.materiales = json.load(file)

        if os.path.exists("prestamos.txt"):
            with open("prestamos.txt", "r") as file:
                self.prestamos = json.load(file)

    def guardar_datos(self):
        """Guarda los datos en archivos de texto al cerrar el programa."""
        with open("usuarios.txt", "w") as file:
            json.dump(self.usuarios, file)

        with open("materiales.txt", "w") as file:
            json.dump(self.materiales, file)

        with open("prestamos.txt", "w") as file:
            json.dump(self.prestamos, file)

        # Cerrar la ventana después de guardar los datos
        self.root.destroy()

    def registrar_usuario(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Usuario")

        tk.Label(top, text="DNI").grid(row=0, column=0)
        entry_dni = tk.Entry(top)
        entry_dni.grid(row=0, column=1)

        tk.Label(top, text="Nombre").grid(row=1, column=0)
        entry_nombre = tk.Entry(top)
        entry_nombre.grid(row=1, column=1)

        tk.Label(top, text="Primer Apellido").grid(row=2, column=0)
        entry_apellido = tk.Entry(top)
        entry_apellido.grid(row=2, column=1)

        tk.Label(top, text="Correo Electrónico").grid(row=3, column=0)
        entry_correo = tk.Entry(top)
        entry_correo.grid(row=3, column=1)

        tk.Label(top, text="Teléfono").grid(row=4, column=0)
        entry_telefono = tk.Entry(top)
        entry_telefono.grid(row=4, column=1)

        def guardar_usuario():
            dni = entry_dni.get()
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            correo = entry_correo.get()
            telefono = entry_telefono.get()

            if not dni or not nombre or not apellido or not correo or not telefono:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if dni in self.usuarios or any(usuario["telefono"] == telefono for usuario in self.usuarios.values()):
                messagebox.showerror("Error", "DNI o teléfono ya registrado.")
                return

            self.usuarios[dni] = {
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "telefono": telefono
            }
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            top.destroy()

        tk.Button(top, text="Guardar", command=guardar_usuario).grid(row=5, column=0, columnspan=2)

    def ver_usuarios(self):
        top = tk.Toplevel(self.root)
        top.title("Usuarios Verificados")

        tree = ttk.Treeview(top, columns=("DNI", "Nombre", "Apellido", "Correo", "Teléfono"), show='headings')
        tree.heading("DNI", text="DNI")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Apellido", text="Apellido")
        tree.heading("Correo", text="Correo")
        tree.heading("Teléfono", text="Teléfono")

        for dni, info in self.usuarios.items():
            tree.insert("", "end", values=(dni, info["nombre"], info["apellido"], info["correo"], info["telefono"]))

        tree.pack(fill="both", expand=True)

    def ver_materiales(self):
        disponibles = "\n".join([f"{material}: {'Disponible' if estado else 'No disponible'}" for material, estado in self.materiales.items()])
        messagebox.showinfo("Materiales Disponibles", disponibles)

    def ver_prestamos(self):
        top = tk.Toplevel(self.root)
        top.title("Préstamos Actuales")

        tree = ttk.Treeview(top, columns=("DNI", "Material", "Fecha"), show='headings')
        tree.heading("DNI", text="DNI")
        tree.heading("Material", text="Material")
        tree.heading("Fecha", text="Fecha")

        for prestamo in self.prestamos:
            tree.insert("", "end", values=(prestamo["dni"], prestamo["material"], prestamo["fecha"]))

        tree.pack(fill="both", expand=True)

    def nuevo_prestamo(self):
        top = tk.Toplevel(self.root)
        top.title("Nuevo Préstamo")

        tk.Label(top, text="DNI Solicitante").grid(row=0, column=0)
        entry_dni = tk.Entry(top)
        entry_dni.grid(row=0, column=1)

        tk.Label(top, text="ID Material").grid(row=1, column=0)
        entry_material = tk.Entry(top)
        entry_material.grid(row=1, column=1)

        def realizar_prestamo():
            dni = entry_dni.get()
            material = entry_material.get()

            if dni not in self.usuarios:
                messagebox.showerror("Error", "El usuario no está registrado.")
                return

            if material not in self.materiales or not self.materiales[material]:
                messagebox.showerror("Error", "El material no está disponible.")
                return

            self.prestamos.append({
                "dni": dni,
                "material": material,
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            self.materiales[material] = False
            messagebox.showinfo("Éxito", "Préstamo registrado con éxito.")
            top.destroy()

        tk.Button(top, text="Prestar", command=realizar_prestamo).grid(row=2, column=0, columnspan=2)

    def devolver_material(self):
        material = simpledialog.askstring("Devolver Material", "Ingrese el ID del material a devolver:")

        if not material or material not in self.materiales:
            messagebox.showerror("Error", "Material no válido.")
            return

        prestamo = next((p for p in self.prestamos if p["material"] == material), None)

        if not prestamo:
            messagebox.showerror("Error", "No se encontró un préstamo para este material.")
            return

        self.prestamos.remove(prestamo)
        self.materiales[material] = True
        messagebox.showinfo("Éxito", "Material devuelto con éxito.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrestamoMaterial(root)
    root.mainloop()
