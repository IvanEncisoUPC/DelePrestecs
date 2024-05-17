from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

#root = Tk()

root = customtkinter.CTk()

root.title("Pruebas")
root.geometry("700x450")

def input():
    dialog = customtkinter.CTkInputDialog(text="Introduce un texto", title="Introduce un texto")
    cosa = dialog.get_input()
    if cosa:
        Label.configure(text=f"Hola {cosa}")

def new():
    new_window = customtkinter.CTkToplevel(root)
    new_window.title("Ventana nueva")
    new_window.geometry("400x200")
    new_window.resizable(False, False) # Width, Height

    def close():
        new_window.destroy()
        new_window.update()

    new_button = customtkinter.CTkButton(new_window, text="Cerrar", command=close)
    new_button.pack(pady=20)

boton1 = customtkinter.CTkButton(root, text="Boton1", command=input)
boton1.pack(pady=40)

boton2 = customtkinter.CTkButton(root, text="Boton2", command=new)
boton2.pack(pady=60)

Label  = customtkinter.CTkLabel(root, text="")
Label.pack(pady=20)

root.mainloop()
