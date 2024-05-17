import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dele_logo_single.png")), size=(26, 26))
        self.dele_large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dele_large_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.return_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "return.png")), size=(20, 20))
        self.material_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "material.png")), size=(20, 20))
        self.users_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "users.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  DELESEIAAT", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.return_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Prestecs",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.return_image, anchor="w", command=self.return_button_event)
        self.return_button.grid(row=2, column=0, sticky="ew")

        self.return_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Materials",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.material_image, anchor="w", command=self.material_button_event)
        self.material_button.grid(row=3, column=0, sticky="ew")

        self.users_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Usuaris",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.users_image, anchor="w", command=self.users_button_event)
        self.users_button.grid(row=4, column=0, sticky="ew")

        # create home frame
        self.return_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.return_frame.grid_columnconfigure(0, weight=1)

        self.return_frame_large_image_label = customtkinter.CTkLabel(self.return_frame, text="", image=self.dele_large_image)
        self.return_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.return_frame_button_1 = customtkinter.CTkButton(self.return_frame, text="Nou Prestec")
        self.return_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.return_frame_button_2 = customtkinter.CTkButton(self.return_frame, text="Devolucio")
        self.return_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.return_button.configure(fg_color=("gray75", "gray25") if name == "Prestecs" else "transparent")
        self.material_button.configure(fg_color=("gray75", "gray25") if name == "Materials" else "transparent")
        self.users_button.configure(fg_color=("gray75", "gray25") if name == "Usuaris" else "transparent")

        # show selected frame
        if name == "Prestecs":
            self.return_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.return_frame.grid_forget()
        if name == "Materials":
            self.material_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.material_frame.grid_forget()
        if name == "Usuaris":
            self.users_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.users_frame.grid_forget()

    def return_button_event(self):
        self.select_frame_by_name("Prestecs")

    def material_button_event(self):
        self.select_frame_by_name("Materials")

    def users_button_event(self):
        self.select_frame_by_name("Usuaris")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode("Light")


if __name__ == "__main__":
    app = App()
    app.mainloop()

