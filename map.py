import numpy
from colorama import Fore, Back, Style
import plant


from numpy import random


class map:
    def __init__(self, dimX, dimY):
        self.dimX = dimX
        self.dimY = dimY
        self.map = [[0] * dimY for i in range(dimX)]
        for x in range(self.dimX):
            for y in range(self.dimY):
                # 0: grass, 1: shrub, 2: bush , 3: tree


                tileType = random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])
                
                match tileType:
                    case 0:
                        plantObj = plant.plant("grass",x,y,self,0.75)
                    case 1:
                        plantObj = plant.plant("shrub",x,y,self,4)
                    case 2:
                        plantObj = plant.plant("bush",x,y,self,5)
                    case 3:
                        plantObj = plant.plant("tree",x,y,self,15)

                self.map[x][y] = {"type": plantObj, "onIt": []}
    
        self.animals =  set()
        self.growing = set()
    
    def getOnIt(self,x,y):
        return self.map[x][y]['onIt']
    
    def addAnimal(self,animal):
        self.animals.add(animal)

    def removeAnimal(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)


    def updateOnIt(self,x,y,cond,id):
        if cond == 1:
            self.map[x][y]['onIt'].append(id)
        else:
            if id in self.map[x][y]['onIt']:
                self.map[x][y]['onIt'].remove(id)

    def inRange(self,x,y):
        return x >= 0 and x < self.dimX and y >= 0 and y < self.dimY

    def getType(self,x,y):
        return self.map[x][y]['type']

    def updateType(self,x,y,type):
        self.map[x][y]['type'] = type

    def printMap(self):
        for x in range(self.dimX):
            print(Style.RESET_ALL)

            for y in range(self.dimY):
                if len(self.map[x][y]['onIt']) == 0:
                    curType = self.map[x][y]['type'].species

                    match curType:
                        case 'grass':
                            back = Back.GREEN
                            fore = Fore.BLACK
                            style = Style.DIM
                        case 'shrub':
                            back = Back.GREEN
                            fore = Fore.YELLOW
                            style = Style.NORMAL
                        case 'bush':
                            back = Back.GREEN
                            fore = Fore.RED
                            style = Style.NORMAL
                        case 'tree':
                            back = Back.GREEN
                            fore = Fore.CYAN
                            style = Style.DIM
                    
                    print(back + fore + style + str(curType)[:1], end = ' ')

                else:
                    species = self.map[x][y]['onIt'][0].species

                    match species:
                        case "rabbit":
                            print(Back.WHITE + Fore.BLACK + Style.NORMAL + species[:1], end = ' ')
                        case "fox":
                            print(Back.WHITE + Fore.RED + Style.NORMAL + species[:1], end = ' ')
                            
        print(Style.RESET_ALL)


    def getdimX(self):
        return self.dimX

    def getdimY(self):
        return self.dimY
