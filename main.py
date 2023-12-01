from PyQt5.QtWidgets import QApplication

from drone_monitoring import ClientVoliere


class Interface:
    pass


def save_case_file():
    pass

def start_mission():
    pass

if __name__ == "__main__":

    app = QApplication()
    client_voliere = ClientVoliere()
    interface = Interface()

    #Connecter les données des drones de la volière avec votre interface
    client_voliere.drone_data.connect(interface.drone_date_updated)

    # 1 quand la vue est créée en qu'on clique sur le bouton GO on sauve le fichier .json (pour le tester)
    interface.start_mission.connect(save_case_file)

    #2 ensuite on va essayer de lancer gflow
    #interface.start_mission.connect(start_mission)

    #on affiche l'interface
    interface.show()
    app.exec()



