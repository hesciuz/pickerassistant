import tkinter

class centrar_ventana:

    def __init__(self, root, ancho_pantalla, largo_pantalla):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_cordenada = int((self.screen_width/2) - (ancho_pantalla/2))
        self.y_cordenada = int((self.screen_height/2) - (largo_pantalla/2))
        self.centrado = "{}x{}+{}+{}".format(ancho_pantalla, largo_pantalla, self.x_cordenada, self.y_cordenada)

    def __str__(self):
        return self.centrado
    

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry(centrar_ventana(root, 1280, 720).__str__())
    root.mainloop()