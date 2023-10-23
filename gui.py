import tkinter
from centrar_ventana_tkinter import centrar_ventana
from add import *
from champ_data import *
import pickle
from  CTkMessagebox import CTkMessagebox

class PickerAssistant:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry(centrar_ventana(self.root, 1280,720).__str__())
        self.root.title("Picker Assistant")
        self.root.configure(background="#020b14")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing_root)
        self.root.wm_iconbitmap(self.resource_path("champ_icon.ico"))

        with open(self.resource_path("memory.dat"), "rb") as pickle_read:
            self.lista_campeones_guardados = pickle.load(pickle_read)

        self.champ_frame = tkinter.Frame(master=self.root, width=750, height=450, background="#917746")
        self.champ_frame.place(x=50, y=50)
        self.champ_frame.grid_propagate(False)

        self.win = tkinter.Label(master=self.root, text="WIN", fg="#a09b8c", font=("Helvetica", 30), background="#020b14")
        self.win.place(x=900, y=50)

        self.lose = tkinter.Label(master=self.root, text="LOSE", fg="#a09b8c", font=("Helvetica", 30), background="#020b14")
        self.lose.place(x=1050, y=50)

        self.win_counter = tkinter.Label(master=self.root, text=self.lista_campeones_guardados[15], fg="#a09b8c", background="#020b14",  font=("Helvetica", 50))
        self.win_counter.place(x=925, y=110)

        self.lose_counter = tkinter.Label(master=self.root, text=self.lista_campeones_guardados[16], fg="#a09b8c", background="#020b14",  font=("Helvetica", 50))
        self.lose_counter.place(x=1080, y=110)

        self.win_plus = tkinter.Button(master=self.root, text="+", fg="#020b14", height=1, width=2, background="#917746", activebackground="#c6923c", font=("Helvetica", 20), command=self.sum_win)
        self.win_plus.place(x=900, y=200)
        self.win_less = tkinter.Button(master=self.root, text="-", fg="#020b14", height=1, width=2, background="#917746", activebackground="#c6923c", font=("Helvetica", 20), command=self.sub_win)
        self.win_less.place(x=950, y=200)

        self.lose_plus = tkinter.Button(master=self.root, text="+", fg="#020b14", height=1, width=2, background="#917746", activebackground="#c6923c", font=("Helvetica", 20), command=self.sum_lose)
        self.lose_plus.place(x=1060, y=200)
        self.lose_plus = tkinter.Button(master=self.root, text="-", fg="#020b14", height=1, width=2, background="#917746", activebackground="#c6923c", font=("Helvetica", 20), command=self.sub_lose)
        self.lose_plus.place(x=1110, y=200)

        #AQUI DEBO MANEJAR UN IMPLEMENTAR PICKLE PARA PODER GUARDAR LOS OBJETOS QUE ESTARAN A CONTINUACION
        #LOS DATOS QUE GUARDARE SERA UNA LISTA DE NOMBRES TIPO STRING, Y AÑADURE UN DATO EN LA CREACION DE LOS add() QUE SERA EL NOMBRE DEL CAMPEON(STRING)
        #SI ESTE ES "" ENTONCES SE CREARA EL BOTON BASE Y SI ESTE ES EL NOMBRE DE UN CAMPEON SE PONDRA EN LA VENTAN
        #PASO 1: USAR UN ARCHIVO DE PYTHON NUEVO QUE SOLO CREE Y GUARDE LOS 15 CAMPEONES("add()) EN UNA LISTA

        self.campeon1 = add(self.champ_frame, self.lista_campeones_guardados[0], 75,75)
        self.campeon2 = add(self.champ_frame, self.lista_campeones_guardados[1], 75,150)
        self.campeon3 = add(self.champ_frame, self.lista_campeones_guardados[2], 75,225)
        self.campeon4 = add(self.champ_frame, self.lista_campeones_guardados[3], 75,300)
        self.campeon5 = add(self.champ_frame, self.lista_campeones_guardados[4], 75,375)
        self.campeon6 = add(self.champ_frame, self.lista_campeones_guardados[5], 150,75)
        self.campeon7 = add(self.champ_frame, self.lista_campeones_guardados[6], 150,150)
        self.campeon8 = add(self.champ_frame, self.lista_campeones_guardados[7], 150,225)
        self.campeon9 = add(self.champ_frame, self.lista_campeones_guardados[8], 150,300)
        self.campeon10 = add(self.champ_frame, self.lista_campeones_guardados[9], 150,375)
        self.campeon11 = add(self.champ_frame, self.lista_campeones_guardados[10], 225,75)
        self.campeon12 = add(self.champ_frame, self.lista_campeones_guardados[11], 225,150)
        self.campeon13 = add(self.champ_frame, self.lista_campeones_guardados[12], 225,225)
        self.campeon14 = add(self.champ_frame, self.lista_campeones_guardados[13], 225,300)
        self.campeon15 = add(self.champ_frame, self.lista_campeones_guardados[14], 225,375)

        self.lista_campeones_mostrados = [self.campeon1,
                                        self.campeon2, self.campeon3,
                                        self.campeon4, self.campeon5,
                                        self.campeon6, self.campeon7,
                                        self.campeon8, self.campeon9,
                                        self.campeon10, self.campeon11,
                                        self.campeon12, self.campeon13,
                                        self.campeon14, self.campeon15]

    def sum_win(self):
        self.win_counter.configure(text=self.win_counter.cget("text")+1)

        if self.win_counter.cget("text") > 9 and self.win_counter.cget("text") < 100:
            self.win_counter.place(x=900, y=110)
        if self.win_counter.cget("text") > 99:
            self.win_counter.place(x=885, y=110)

    def sub_win(self):  
        if self.win_counter.cget("text") != 0:
            self.win_counter.configure(text=self.win_counter.cget("text")-1)

        if self.win_counter.cget("text") < 10:
            self.win_counter.place(x=925, y=110)
        elif self.win_counter.cget("text") < 100:
            self.win_counter.place(x=900, y=110)


    def sum_lose(self):
        self.lose_counter.configure(text=self.lose_counter.cget("text")+1)

        if self.lose_counter.cget("text") > 9 and self.lose_counter.cget("text") < 100:
            self.lose_counter.place(x=1060, y=110)
        elif self.lose_counter.cget("text") > 99:
            self.lose_counter.place(x=1045, y=110)

    def sub_lose(self):
        if self.lose_counter.cget("text") != 0:
            self.lose_counter.configure(text=self.lose_counter.cget("text")-1)

        if self.lose_counter.cget("text") < 10:
            self.lose_counter.place(x=1080, y=110)
        elif self.lose_counter.cget("text") < 100:
            self.lose_counter.place(x=1060, y=110)

    def on_closing_root(self):
        for i in range(15):
            self.lista_campeones_guardados[i].nombre_campeon = self.lista_campeones_mostrados[i].nombre_campeon
            self.lista_campeones_guardados[i].nota_campeon = self.lista_campeones_mostrados[i].nota_campeon
            self.lista_campeones_guardados[i].win_against = self.lista_campeones_mostrados[i].win_against
            self.lista_campeones_guardados[i].lose_against = self.lista_campeones_mostrados[i].lose_against
            print(f"Datos Guardados del campeon #{i+1} guardados.")
        self.lista_campeones_guardados[15] = int(self.win_counter.cget("text"))
        self.lista_campeones_guardados[16] = int(self.lose_counter.cget("text"))
        with open(self.resource_path("memory.dat"), "wb") as pickle_write:
            pickle.dump(self.lista_campeones_guardados, pickle_write)
        self.root.destroy()

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
    PickerAssistant().root.mainloop()