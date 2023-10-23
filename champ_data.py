

class champ_data:

    def __init__(self):
        self.nombre_campeon = ""
        self.nota_campeon = "Escribe aqui tus notas personales."
        self.win_against = ["","","","","","","","","",""]
        self.lose_against = ["","","","","","","","","",""]

if __name__ == "__main__":
    test_object = champ_data()
    print(test_object.win_against)