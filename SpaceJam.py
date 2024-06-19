from direct.showbase.ShowBase import ShowBase
import math, random
import SpaceJamClasses 
import DefensePaths


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        SetupScene(self)
        #self.DrawCloudDefense(self.Planet1, nickName)
        #self.DrawBaseballSeams(self.SpaceStation1, nickName, j, fullCycle, 2)

        

def SetupScene(self):

    #UNIVERSE
    self.Universe = SpaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/universe.jpg", (0, 0, 0), 25000)

    #PLANETS
    self.Planet1 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/earth.jpg",      (1000,      10,     -1000),     1000)
    self.Planet2 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/loaf.jpg",       (3000,     100,    -3000),    1000)
    self.Planet3 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/mars.jpg",       (21000,     1000,   -7000),     1100)
    self.Planet4 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "./Assets/Planets/purple.jpg",     (-7000,     10,     21000),     1000)
    self.Planet5 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/saturn.jpg",     (-14000,    100,    14000),     1000)
    self.Planet6 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/shamrock.jpg",   (-21000,    1000,   7000),      1000)

    self.SpaceStation1 = SpaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation1B/spaceStation.egg", self.render, "Space Station", "./Assets/Space Station/SpaceStation1B/SpaceStation1_Dif2.png", (0, 0, 0), 10000)

    self.Hero = SpaceJamClasses.Player(self.loader, "./Assets/Dumbledore/Dumbledore.egg", self.render, "Player", "./Assets/Dumbledore/spacejet_C.png", (0, 0, 0), 100)

    for i in range(100):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawBaseballSeams(self, self.Planet1, droneName, step, 50)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1

    for i in range(200):
        step = i
        droneName = 'drone' + str(i)
        droneCoords = DrawXSeams(self, self.Planet2, droneName, step, 150)
        self.DroneObj = SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", droneCoords, 5)
        i = i + 1


def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 4):
    unitVec = DefensePaths.BaseballSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position

def DrawXSeams(self, centralObject, droneName, step, numSeams, radius = 4):
    unitVec = DefensePaths.XSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    return position
    
def DrawCloudDefense(self, centralObject, droneName):
    unitVec = DefensePaths.Cloud()
    unitVec.normalize()
    position = unitVec * 500 + centralObject.modelNode.getPos()
    SpaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)

    fullCycle = 60

    for j in range(fullCycle):
        SpaceJamClasses.Drone.droneCount += 1
        nickName = "Drone" + str(SpaceJamClasses.Drone.droneCount)
    

    #self.disableMouse


app = MyApp()
app.run()