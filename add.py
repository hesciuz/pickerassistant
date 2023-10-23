import sys
import os
from centrar_ventana_tkinter import centrar_ventana
import tkinter
import tkinter.ttk
from  CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image
import champ_data

class add:
    lista_campeones = ['Ninguno', 'Aatrox','Ahri', 'Akali', 'Akshan','Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 
            'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Belveth', 'Blitzcrank', 'Brand', 
            'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 
            'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 
            'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 
            'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 
            'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 
            'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 
            'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", "K'Sante", 'LeBlanc', 'Lee Sin', 
            'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 
            'Maokai', 'Maestro Yi', 'Milio', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Naafiri', 'Nami', 'Nasus', 
            'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu y Willump', 'Olaf', 'Orianna', 
            'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata',
            'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 
            'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 
            'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 
            'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 
            'Vayne', 'Veigar', "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 
            'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 
            'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
    lista_busqueda_imagenes = ['Ninguno', 'Aatrox','Ahri', 'Akali', 'Akshan','Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 
            'Ashe', 'AurelionSol', 'Azir', 'Bard', 'Belveth', 'Blitzcrank', 'Brand', 
            'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "ChoGath", 'Corki', 
            'Darius', 'Diana', 'Draven', 'DrMundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 
            'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 
            'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 
            'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "KaiSa", 
            'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 
            'Kennen', "KhaZix", 'Kindred', 'Kled', "KogMaw", "KSante", 'LeBlanc', 'LeeSin', 
            'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 
            'Maokai', 'MasterYi', 'Milio', 'MissFortune', 'Mordekaiser', 'Morgana', 'Naafiri', 'Nami', 'Nasus', 
            'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 
            'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "RekSai", 'Rell', 'Renata',
            'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 
            'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 
            'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 
            'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 
            'Vayne', 'Veigar', "VelKoz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 
            'Wukong', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 
            'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
    lista_counters = ['Ninguno', 'Aatrox','Ahri', 'Akali', 'Akshan','Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 
            'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Belveth', 'Blitzcrank', 'Brand', 
            'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 
            'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 
            'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 
            'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 
            'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 
            'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 
            'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", "K'Sante", 'LeBlanc', 'Lee Sin', 
            'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 
            'Maokai', 'Maestro Yi', 'Milio', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Naafiri', 'Nami', 'Nasus', 
            'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu y Willump', 'Olaf', 'Orianna', 
            'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata',
            'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 
            'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 
            'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 
            'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 
            'Vayne', 'Veigar', "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 
            'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 
            'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

    def __init__(self, root, object_campeon, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.nombre_campeon = object_campeon.nombre_campeon
        self.nota_campeon = object_campeon.nota_campeon
        self.win_against = object_campeon.win_against
        self.lose_against = object_campeon.lose_against
        self.champ = tkinter.Frame(master=root, width=150, height=150)
        self.champ_button = tkinter.Button(master=self.champ, text="+", fg="#020b14", bg="#917746", activebackground="#c6923c", font=("",100), command=self.elegir_campeon_main)

        self.champ.grid_propagate(False)
        self.champ.columnconfigure(0, weight=1)
        self.champ.rowconfigure(0,weight=1)
        self.champ.grid(row=x, column=y) #put frame where the button should be
        self.champ_button.grid(sticky="wens")

        if self.nombre_campeon != "":
            indice_campeon = self.lista_busqueda_imagenes.index(self.nombre_campeon)
            image_location = os.path.abspath(".") + "\Avatar\{}.png".format(self.lista_busqueda_imagenes[indice_campeon])
            self.imagen = ImageTk.PhotoImage(Image.open(image_location))
            self.champ_button.config(text="", image=self.imagen, compound='center', command=self.vista)
        
    def elegir_campeon_main(self):
        def funcion_aceptar():
            if self.campeones.get() == "Ninguno":
                self.campeones.destroy()
                self.toplevel.destroy()
            
            elif self.campeones.get() in self.lista_campeones and self.campeones.get() != "Ninguno":
                image_location = os.path.abspath(".") + "\Avatar\{}.png".format(self.lista_busqueda_imagenes[self.campeones.current()])
                self.nombre_campeon = self.lista_busqueda_imagenes[self.campeones.current()]
                self.imagen = ImageTk.PhotoImage(Image.open(image_location))
                self.champ_button.config(text="", image=self.imagen, compound='center', command=self.vista)
                self.toplevel.destroy()


        self.toplevel = tkinter.Toplevel(master=self.root)
        self.screen_width = self.toplevel.winfo_screenwidth()
        self.screen_height = self.toplevel.winfo_screenheight()
        self.x_cordenada = int((self.screen_width/2) - (300/2))
        self.y_cordenada = int((self.screen_height/2) - (240/2))
        self.toplevel.geometry("300x240+{}+{}".format(self.x_cordenada, self.y_cordenada))
        self.toplevel.title("Elige un camepeon")
        self.toplevel.configure(background="#020b14")
        self.toplevel.resizable(False, False)
        self.toplevel.grab_set()
        self.toplevel.wm_iconbitmap(self.resource_path("champ_icon.ico"))

        self.campeones = tkinter.ttk.Combobox(master=self.toplevel, state="readonly", width=20,values=self.lista_campeones)
        self.campeones.set("Ninguno")
        self.campeones.place(x=150, y=50, anchor="center")

        self.aceptar_campeon = tkinter.Button(master=self.toplevel, text="Aceptar", font=("",15), fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", command=funcion_aceptar)
        self.aceptar_campeon.place(x=150, y=150,anchor="center")

    def elegir_campeon_win_against(self, label, indice):
        def funcion_aceptar():
            if self.campeones.get() == "Ninguno":
                self.win_against[indice] = ""
                label.configure(font=("",24), text="+")
                self.toplevel_win_against.destroy()
                self.toplevel_vista.grab_set()
            else:
                self.win_against[indice] = self.campeones.get()
                label.configure(font=("",24), text=self.campeones.get())
                if len(label.cget("text")) <= 7:
                    label.configure(text=self.campeones.get())
                elif len(label.cget("text")) >= 8:
                    label.configure(font=("", 14), text=self.campeones.get())
                elif len(label.cget("text")) >= 10:
                    label.configure(font=("", 2), text=self.campeones.get())
                self.toplevel_win_against.destroy()
                self.toplevel_vista.grab_set()
        def on_closing_function1():
            self.toplevel_win_against.destroy()
            self.toplevel_vista.grab_set()


        self.toplevel_win_against = tkinter.Toplevel(master=self.root)
        self.screen_width = self.toplevel_win_against.winfo_screenwidth()
        self.screen_height = self.toplevel_win_against.winfo_screenheight()
        self.x_cordenada = int((self.screen_width/2) - (300/2))
        self.y_cordenada = int((self.screen_height/2) - (240/2))
        self.toplevel_win_against.geometry("300x240+{}+{}".format(self.x_cordenada, self.y_cordenada))
        self.toplevel_win_against.title("Elige un camepeon")
        self.toplevel_win_against.configure(background="#020b14")
        self.toplevel_win_against.resizable(False, False)
        self.toplevel_win_against.protocol("WM_DELETE_WINDOW", on_closing_function1)
        self.toplevel_win_against.grab_set()
        self.toplevel_win_against.wm_iconbitmap(self.resource_path("champ_icon.ico"))

        self.campeones = tkinter.ttk.Combobox(master=self.toplevel_win_against, state="readonly", width=20,values=self.lista_counters)
        self.campeones.set("Ninguno")
        self.campeones.place(x=150, y=50, anchor="center")

        self.aceptar_campeon = tkinter.Button(master=self.toplevel_win_against, text="Aceptar", font=("",15), fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", command=funcion_aceptar)
        self.aceptar_campeon.place(x=150, y=150,anchor="center")
        
    def elegir_campeon_lose_against(self, label, indice):
        def funcion_aceptar():
            if self.campeones.get() == "Ninguno":
                self.lose_against[indice] = ""
                label.configure(font=("",24), text="+")
                self.toplevel_lose_against.destroy()
                self.toplevel_vista.grab_set()
            else:
                self.lose_against[indice] = self.campeones.get()
                label.configure(font=("",24), text=self.campeones.get())
                if len(label.cget("text")) <= 7:
                    label.configure(text=self.campeones.get())
                elif len(label.cget("text")) >= 8:
                    label.configure(font=("", 14), text=self.campeones.get())
                elif len(label.cget("text")) >= 10:
                    label.configure(font=("", 2), text=self.campeones.get())
                self.toplevel_lose_against.destroy()
                self.toplevel_vista.grab_set()
        def on_closing_function2():
            self.toplevel_lose_against.destroy()
            self.toplevel_vista.grab_set()


        self.toplevel_lose_against = tkinter.Toplevel(master=self.root)
        self.screen_width = self.toplevel_lose_against.winfo_screenwidth()
        self.screen_height = self.toplevel_lose_against.winfo_screenheight()
        self.x_cordenada = int((self.screen_width/2) - (300/2))
        self.y_cordenada = int((self.screen_height/2) - (240/2))
        self.toplevel_lose_against.geometry("300x240+{}+{}".format(self.x_cordenada, self.y_cordenada))
        self.toplevel_lose_against.title("Elige un camepeon")
        self.toplevel_lose_against.configure(background="#020b14")
        self.toplevel_lose_against.resizable(False, False)
        self.toplevel_lose_against.protocol("WM_DELETE_WINDOW", on_closing_function2)
        self.toplevel_lose_against.grab_set()
        self.toplevel_lose_against.wm_iconbitmap(self.resource_path("champ_icon.ico"))

        self.campeones = tkinter.ttk.Combobox(master=self.toplevel_lose_against, state="readonly", width=20,values=self.lista_counters)
        self.campeones.set("Ninguno")
        self.campeones.place(x=150, y=50, anchor="center")

        self.aceptar_campeon = tkinter.Button(master=self.toplevel_lose_against, text="Aceptar", font=("",15), fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", command=funcion_aceptar)
        self.aceptar_campeon.place(x=150, y=150,anchor="center")

    def vista(self):
        self.toplevel_vista = tkinter.Toplevel(master=self.root)
        self.toplevel_vista.geometry(centrar_ventana(self.toplevel_vista, 1280, 720).__str__())
        self.toplevel_vista.title(self.nombre_campeon)
        self.toplevel_vista.configure(background="#020b14")
        self.toplevel_vista.resizable(False, False)
        self.toplevel_vista.protocol("WM_DELETE_WINDOW", self.on_closing_vista)
        self.toplevel_vista.wm_iconbitmap(self.resource_path("champ_icon.ico"))

        self.nombre_label = tkinter.Label(master=self.toplevel_vista, bg="#020b14", fg="dark goldenrod", text=self.nombre_campeon, font=("", 30))
        self.nombre_label.place(anchor='center', relx=0.17, rely=0.07)
        self.image_location = self.resource_path("Splashart\{}_0.jpg".format(self.nombre_campeon))
        self.image_frame = tkinter.Frame(master=self.toplevel_vista, background="#917746", width=308, height=560)
        self.image_frame.place(relx=0.05, rely=0.115)
        self.vista_campeon = ImageTk.PhotoImage(Image.open(self.image_location))
        self.image_label = tkinter.Label(master=self.image_frame, border=0, image=self.vista_campeon, background="gray")
        self.image_label.place(x=0, y=0)

        self.nota_textbox = tkinter.Text(master=self.toplevel_vista, wrap='word', width=45, height=25, undo=True, autoseparators=True, maxundo=-1, fg="#d3cbbb", bg="#1e2328", insertbackground='DarkGoldenrod3', font=("Bold",14), borderwidth=0)
        self.nota_textbox.place(relx=0.33, rely=0.115)
        self.nota_textbox.insert("1.0", self.nota_campeon)

        self.win_against_label = tkinter.Label(master=self.toplevel_vista,  bg="#020b14", fg="dark goldenrod", text="Gana contra", font=("", 24))
        self.win_against_label.place(relx=0.74, rely=0.04)
        self.win_against_frame = tkinter.Frame(master=self.toplevel_vista, background="#1e2328", width=280, height=250)
        self.win_against_frame.place(relx=0.74, rely=0.115)
        self.win_against_frame.pack_propagate(False)

        self.label1 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label1, 0)])
        self.label1.place(x=0, y=0, width=140, height=50)
        self.label2 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label2, 1)])
        self.label2.place(x=140, y=0, width=140, height=50)
        self.label3 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label3, 2)])
        self.label3.place(x=0, y=50, width=140, height=50)
        self.label4 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label4, 3)])
        self.label4.place(x=140, y=50, width=140, height=50)
        self.label5 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label5, 4)])
        self.label5.place(x=0, y=100, width=140, height=50)
        self.label6 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label6, 5)])
        self.label6.place(x=140, y=100, width=140, height=50)
        self.label7 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label7, 6)])
        self.label7.place(x=0, y=150, width=140, height=50)
        self.label8 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label8, 7)])
        self.label8.place(x=140, y=150, width=140, height=50)
        self.label9 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label9, 8)])
        self.label9.place(x=0, y=200, width=140, height=50)
        self.label10 = tkinter.Button(master=self.win_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_win_against(self.label10, 9)])
        self.label10.place(x=140, y=200, width=140, height=50)
        self.lista_win = [self.label1,
                        self.label2,
                        self.label3,
                        self.label4,
                        self.label5,
                        self.label6,
                        self.label7,
                        self.label8,
                        self.label9,
                        self.label10]
        
        for i in range(len(self.win_against)):
            if self.win_against[i] != "":
                if len(self.win_against[i]) <= 7:
                    self.lista_win[i].configure(text=self.win_against[i])
                elif len(self.win_against[i]) >= 8:
                    self.lista_win[i].configure(font=("", 14), text=self.win_against[i])
                elif len(self.win_against[i]) >= 10:
                    self.lista_win[i].configure(font=("", 2), text=self.win_against[i])

        # self.añadir_win_against = tkinter.Button(master=self.toplevel, text="+", fg="#020b14", bg="#917746", activebackground="#c6923c", activeforeground="#f3e9d5", command=self.elegir_campeon_win_against)
        # self.añadir_win_against.place(relx=0.85, rely=0.2)

        self.lose_against_label = tkinter.Label(master=self.toplevel_vista,  bg="#020b14", fg="dark goldenrod", text="Pierde contra", font=("", 24))
        self.lose_against_label.place(relx=0.74, rely=0.5)
        self.lose_against_frame = tkinter.Frame(master=self.toplevel_vista, background="#1e2328", width=280, height=250)
        self.lose_against_frame.place(relx=0.74, rely=0.575)
        self.lose_against_frame.pack_propagate(False)

        self.label11 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label11, 0)])
        self.label11.place(x=0, y=0, width=140, height=50)
        self.label12 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label12, 1)])
        self.label12.place(x=140, y=0, width=140, height=50)
        self.label13 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label13, 2)])
        self.label13.place(x=0, y=50, width=140, height=50)
        self.label14 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label14, 3)])
        self.label14.place(x=140, y=50, width=140, height=50)
        self.label15 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label15, 4)])
        self.label15.place(x=0, y=100, width=140, height=50)
        self.label16 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label16, 5)])
        self.label16.place(x=140, y=100, width=140, height=50)
        self.label17 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label17, 6)])
        self.label17.place(x=0, y=150, width=140, height=50)
        self.label18 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label18, 7)])
        self.label18.place(x=140, y=150, width=140, height=50)
        self.label19 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label19, 8)])
        self.label19.place(x=0, y=200, width=140, height=50)
        self.label20 = tkinter.Button(master=self.lose_against_frame, text="+",  fg="#020b14",bg="#917746", activeforeground="#f3e9d5", activebackground="#c6923c", font=("", 24), justify="center", command=lambda: [self.elegir_campeon_lose_against(self.label20, 9)])
        self.label20.place(x=140, y=200, width=140, height=50)
        self.lista_lose = [self.label11,
                        self.label12,
                        self.label13,
                        self.label14,
                        self.label15,
                        self.label16,
                        self.label17,
                        self.label18,
                        self.label19,
                        self.label20]
        
        for i in range(len(self.lose_against)):
            if self.lose_against[i] != "":
                if len(self.lose_against[i]) <= 7:
                    self.lista_lose[i].configure(text=self.lose_against[i])
                elif len(self.lose_against[i]) >= 8:
                    self.lista_lose[i].configure(font=("", 14), text=self.lose_against[i])
                elif len(self.lose_against[i]) >= 10:
                    self.lista_lose[i].configure(font=("", 2), text=self.lose_against[i])

        self.delete_button = tkinter.Button(master=self.toplevel_vista, text="eliminar campeon", fg="#020b14", bg="#917746", activebackground="#c6923c", activeforeground="#f3e9d5", command=self.reiniciar_funcion)
        self.delete_button.place(relx=0.8445, rely=0.95)

        self.toplevel_vista.grab_set()

    def reiniciar_funcion(self):
        eleccion = CTkMessagebox(title="Confirmar", message="¿Desea realmente eliminar al campeón? \nSe perderan todos los datos.",
                        icon="question", option_2="Si", option_1="No")

        if eleccion.get() == "Si":
            self.champ_button.destroy()
            self.champ_button = tkinter.Button(master=self.champ, text="+", fg="#020b14", bg="#917746", activebackground="#c6923c", font=("",100), command=self.elegir_campeon_main)
            self.nombre_campeon = ""
            self.nota_campeon = "Escribe aqui tus notas personales."
            self.win_against = ["","","","","","","","","",""]
            self.lose_against = ["","","","","","","","","",""]
            self.champ.grid_propagate(False)
            self.champ.columnconfigure(0, weight=1)
            self.champ.rowconfigure(0,weight=1)
            self.champ.grid(row=self.x, column=self.y)
            self.champ_button.grid(sticky="wens")
            self.toplevel_vista.destroy()

    def on_closing_vista(self):
        self.nota_campeon = self.nota_textbox.get("1.0", "end-1c")
        self.toplevel_vista.destroy()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
            # print(base_path) 
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    test = tkinter.Tk()
    test.resizable(False,False)
    campeon = champ_data.champ_data()
    add(test, campeon, 75, 75)
    test.mainloop()