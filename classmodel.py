import json

class Building:
    def __init__(self,name,verticies):
        self.name = name
        self.verticies = verticies

class Drone:
    def __init__(self, name, posit, target, orient):
        self.name = name
        self.posit = posit
        self.target = target
        self.orient = orient



class Modele:
    def __init__(self):
        self.builings=[]
        self.drones=[]

    def add_building(self,build):
        self.buildings.append(build)

    def add_drone(self,drone):
        self.drones.append(drone)


building1 = (1, 3)
dico_bat={
        "name": building1[0],
        "verticies" :building1[1]
}

drone1=(1,3,2,1)
dico_drone={
            "name":drone1[0],
            "position":drone1[1],
            "target":drone1[2],
            "orientation":drone1[3]
}

with open('data.json', 'w') as mon_fichier:
	json.dump(dico_bat, mon_fichier)
	json.dump(dico_drone, mon_fichier)

