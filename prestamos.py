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

        self.title("DelePrestecs Alpha 0.7")
        self.iconbitmap('img/dele.ico')
        self.geometry("700x450")
        self.resizable(False, False) # Width, Height

        # Cargamos los datos
        self.usuarios = {}
        self.materiales = {}
        self.prestecs = {}

        self.cargar_datos()

        # Creamos un grid 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Cargamos las imágenes
        self.logo_img = customtkinter.CTkImage(Image.open('img/dele.png'), size=(26, 26))
        self.deleprestecs_img = customtkinter.CTkImage(Image.open("img/deleprestecs.png"), size=(500, 150))
        self.prestec_img = customtkinter.CTkImage(Image.open("img/prestec.png"), size=(20, 20))
        self.material_img = customtkinter.CTkImage(Image.open("img/material.png"), size=(20, 20))
        self.usuaris_img = customtkinter.CTkImage(Image.open("img/usuaris.png"), size=(20, 20))

        # Creamos el frame de navegación
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="DELESEIAAT", image=self.logo_img, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.prestecs_button = customtkinter.CTkButton(self.navigation_frame, 
                                                       corner_radius=0, 
                                                       height=40, 
                                                       border_spacing=10, 
                                                       text="Prestecs",
                                                       fg_color="transparent", 
                                                       text_color=("gray10", "gray90"), 
                                                       hover_color=("gray70", "gray30"),
                                                       image=self.prestec_img, 
                                                       anchor="w",
                                                       command=self.prestecs_button_event)
        self.prestecs_button.grid(row=1, column=0, sticky="ew")

        self.materials_button = customtkinter.CTkButton(self.navigation_frame, 
                                                       corner_radius=0, 
                                                       height=40, 
                                                       border_spacing=10, 
                                                       text="Materials",
                                                       fg_color="transparent", 
                                                       text_color=("gray10", "gray90"), 
                                                       hover_color=("gray70", "gray30"),
                                                       image=self.material_img, 
                                                       anchor="w",
                                                       command=self.materials_button_event)
        self.materials_button.grid(row=2, column=0, sticky="ew")

        self.usuaris_button = customtkinter.CTkButton(self.navigation_frame, 
                                                       corner_radius=0, 
                                                       height=40, 
                                                       border_spacing=10, 
                                                       text="Usuaris",
                                                       fg_color="transparent", 
                                                       text_color=("gray10", "gray90"), 
                                                       hover_color=("gray70", "gray30"),
                                                       image=self.usuaris_img, 
                                                       anchor="w",
                                                       command=self.usuaris_button_event)
        self.usuaris_button.grid(row=3, column=0, sticky="ew")

         # create frame prestecs
        self.prestecs_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.prestecs_frame.grid_columnconfigure(0, weight=1)

        self.prestecs_frame_img = customtkinter.CTkLabel(self.prestecs_frame, text="", image=self.deleprestecs_img)
        self.prestecs_frame_img.grid(row=0, column=0, padx=20, pady=10)
        self.prestecs_frame_prestecs_list_button = customtkinter.CTkButton(self.prestecs_frame, text="Llista de prestecs",height=50, width=250, font = ("Helvetica", 24), command=self.prestecs_frame_prestecs_list_button_event)
        self.prestecs_frame_prestecs_list_button.grid(row=1, column=0, padx=20, pady=10)
        self.prestecs_frame_prestec_button = customtkinter.CTkButton(self.prestecs_frame, text="Nou prestec",height=50, width=250, font = ("Helvetica", 24), command=self.prestecs_frame_prestec_button_event)
        self.prestecs_frame_prestec_button.grid(row=2, column=0, padx=20, pady=10)
        self.prestecs_frame_retornament_button = customtkinter.CTkButton(self.prestecs_frame, text="Retornament",height=50, width=250, font = ("Helvetica", 24), command=self.prestecs_frame_retornament_button_event)
        self.prestecs_frame_retornament_button.grid(row=3, column=0, padx=20, pady=10)
    

        

        # create frame materials
        self.materials_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.materials_frame.grid_columnconfigure(0, weight=1)

        self.materials_frame_img = customtkinter.CTkLabel(self.materials_frame, text="", image=self.deleprestecs_img)
        self.materials_frame_img.grid(row=0, column=0, padx=20, pady=10)
        self.materials_frame_material_list_button = customtkinter.CTkButton(self.materials_frame, text="Llista de materials",height=50, width=250, font = ("Helvetica", 24))
        self.materials_frame_material_list_button.grid(row=1, column=0, padx=20, pady=10)
        self.materials_frame_material_new_button = customtkinter.CTkButton(self.materials_frame, text="Afegir material",height=50, width=250, font = ("Helvetica", 24))
        self.materials_frame_material_new_button.grid(row=2, column=0, padx=20, pady=10)
        self.materials_frame_material_delete_button = customtkinter.CTkButton(self.materials_frame, text="Eliminar material",height=50, width=250, font = ("Helvetica", 24))
        self.materials_frame_material_delete_button.grid(row=3, column=0, padx=20, pady=10)


        # create frame usuaris
        self.usuaris_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.usuaris_frame.grid_columnconfigure(0, weight=1)

        self.usuaris_frame_img = customtkinter.CTkLabel(self.usuaris_frame, text="", image=self.deleprestecs_img)
        self.usuaris_frame_img.grid(row=0, column=0, padx=20, pady=10)
        self.usuaris_frame_user_list_button = customtkinter.CTkButton(self.usuaris_frame, text="Llista de usuaris",height=50, width=250, font = ("Helvetica", 24))
        self.usuaris_frame_user_list_button.grid(row=1, column=0, padx=20, pady=10)
        self.usuaris_frame_user_new_button = customtkinter.CTkButton(self.usuaris_frame, text="Usuari nou",height=50, width=250, font = ("Helvetica", 24))
        self.usuaris_frame_user_new_button.grid(row=2, column=0, padx=20, pady=10)
        self.usuaris_frame_user_delete_button = customtkinter.CTkButton(self.usuaris_frame, text="Esborrar usuari",height=50, width=250, font = ("Helvetica", 24))
        self.usuaris_frame_user_delete_button.grid(row=3, column=0, padx=20, pady=10)

        # Seleccionamos el frame de inicio
        self.select_frame_by_name("prestecs")

    # Select by frame
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.prestecs_button.configure(fg_color=("gray75", "gray25") if name == "prestecs" else "transparent")
        self.materials_button.configure(fg_color=("gray75", "gray25") if name == "materials" else "transparent")
        self.usuaris_button.configure(fg_color=("gray75", "gray25") if name == "usuaris" else "transparent")

        # show selected frame
        if name == "prestecs":
            self.prestecs_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.prestecs_frame.grid_forget()
        if name == "materials":
            self.materials_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.materials_frame.grid_forget()
        if name == "usuaris":
            self.usuaris_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.usuaris_frame.grid_forget()
    
    # Aqu van las funciones de los botones
    def prestecs_button_event(self):
        self.select_frame_by_name("prestecs")

    def materials_button_event(self):
        self.select_frame_by_name("materials")

    def usuaris_button_event(self):
        self.select_frame_by_name("usuaris")

    def prestecs_frame_prestecs_list_button_event(self):
        # Crear una nueva ventana Toplevel
        top = customtkinter.CTkToplevel(self)
        top.title("Llista de prestecs")
        top.geometry("800x600")
        top.iconbitmap('img/dele.ico')

        # Crear un frame de CustomTkinter dentro del Toplevel
        frame = customtkinter.CTkFrame(top, corner_radius=10)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear un Treeview dentro del frame
        treeview = ttk.Treeview(frame, columns=("A", "B", "C", "D", "E", "F"), show="headings", height=10)
        treeview.pack(pady=20, padx=20, fill="both", expand=True)

        # Definir los encabezados de columna
        treeview.heading("A", text="Material")
        treeview.heading("B", text="Data")
        treeview.heading("C", text="Nom")
        treeview.heading("D", text="Cognom")
        treeview.heading("E", text="DNI")
        treeview.heading("F", text="Telefon")

        # Definir el tamaño de las columnas
        treeview.column("A", width=100)
        treeview.column("B", width=100)
        treeview.column("C", width=100)
        treeview.column("D", width=100)
        treeview.column("E", width=100)
        treeview.column("F", width=100)

        # Agregar algunos datos
        
        for item in self.prestecs:
            treeview.insert("", tk.END, values=item)

    def prestecs_frame_retornament_button_event(slef):
        dialog = customtkinter.CTkInputDialog(text="Introduce DNI del usuario", title="Retornament de material")
    
    def prestecs_frame_prestec_button_event(self):
        finestra_prestec = customtkinter.CTkToplevel(self)
        finestra_prestec.title("Nou Prestec")
        finestra_prestec.geometry("300x200")
        finestra_prestec.resizable(False, False) # Width, Height
        
        def tancar():
            finestra_prestec.destroy()
            finestra_prestec.update()
        
        def enviar():
            dni = dni_entrada.get()
            if dni not in self.usuarios:
                messagebox.showerror("Error", "El usuario no existe.")
                return
            if not any(self.materiales.values()):
                messagebox.showerror("Error", "No hay materiales disponibles.")
                return
            material = next(material for material, disponible in self.materiales.items() if disponible)
            self.materiales[material] = False
            self.prestamos.append({"dni": dni, "material": material, "fecha": datetime.now().isoformat()})
            messagebox.showinfo("Éxito", "Préstamo realizado con éxito.")
            tancar()
        
        dni_entrada = customtkinter.CTkEntry(finestra_prestec, placeholder_text="DNI")
        dni_entrada.pack(pady=10)
        dni_entrada = customtkinter.CTkEntry(finestra_prestec, placeholder_text="IdMaterial")
        dni_entrada.pack(pady=10) 
        okay_button = customtkinter.CTkButton(finestra_prestec, text="OK", command=enviar)
        okay_button.pack(pady=10)
        tancar_button = customtkinter.CTkButton(finestra_prestec, text="Tancar", command=tancar)
        tancar_button.pack(pady=10)

    def cargar_datos(self):
        """Carga los datos de los archivos de texto al iniciar el programa."""
        if os.path.exists("data/usuarios.txt"):
            with open("data/usuarios.txt", "r") as file:
                self.usuarios = json.load(file)

        if os.path.exists("data/materiales.txt"):
            with open("data/materiales.txt", "r") as file:
                self.materiales = json.load(file)

        if os.path.exists("data/prestamos.txt"):
            with open("data/prestamos.txt", "r") as file:
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

if __name__ == "__main__":
    app = App()
    app.mainloop()