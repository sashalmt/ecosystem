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
                        plantObj = plant.plant("grass",x,y,self,1)
                    case 1:
                        plantObj = plant.plant("shrub",x,y,self,3)
                    case 2:
                        plantObj = plant.plant("bush",x,y,self,5)
                    case 3:
                        plantObj = plant.plant("tree",x,y,self,15)

                self.map[x][y] = {"type": plantObj, "onIt": []}
    
        self.animals =  set()
    
    def getOnIt(self,x,y):
        return self.map[x][y]['onIt']
    

    def removeAnimal(self,animal):
        self.animals.remove(animal)


    def updateOnIt(self,x,y,cond,id):
        if cond == 1:
            self.map[x][y]['onIt'].append(id)
        else:
            self.map[x][y]['onIt'].remove(id)


    def getType(self,x,y):
        return self.map[x][y]['type']

    def printMap(self):
        for x in range(self.dimX):
            print(Style.RESET_ALL)

            for y in range(self.dimY):
                if len(self.map[x][y]['onIt']) == 0:
                    curType = self.map[x][y]['type']

                    match curType:
                        case 0:
                            back = Back.GREEN
                            fore = Fore.BLACK
                            style = Style.DIM
                        case 1:
                            back = Back.GREEN
                            fore = Fore.YELLOW
                            style = Style.NORMAL
                        case 2:
                            back = Back.GREEN
                            fore = Fore.RED
                            style = Style.NORMAL
                        case 3:
                            back = Back.GREEN
                            fore = Fore.CYAN
                            style = Style.DIM
                    
                    print(back + fore + style + str(curType), end = ' ')

                else:
                    species = self.map[x][y]['onIt'][0].species

                    match species:
                        case "Rabbit":
                            print(Back.WHITE + Fore.BLACK + Style.NORMAL + species[:1], end = ' ')
                        case "Fox":
                            print(Back.WHITE + Fore.RED + Style.NORMAL + species[:1], end = ' ')
                            
        print(Style.RESET_ALL)
        print('-' * self.dimX)


