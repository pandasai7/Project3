from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
#
#class MyApp(ShowBase):
#    def __init__(self):
#        ShowBase.__init__(self)
#

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Player(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

#app = MyApp()
#app.run()