import random as rnd

class animal:
    def __init__(self,species,x,y,mapObj):
        self.species = species
        self.id = 1
        
        self.x = x
        self.y = y
        
        self.hunger = 2


        self.map = mapObj

        self.map.updateOnIt(x,y,1,self)

    def turn(self):
        self.move()
        self.hunger -= 1
        
        self.eat()
        
        if self.hunger < 0:
            self.die()

    
    def eat(self):
        curType = self.map.getType(self.x,self.y)
        if curType == 1:
            self.hunger += 3
            print('*')


    def move(self):

        self.map.updateOnIt(self.x,self.y,0,self)

        if self.x != 0 and self.x != self.map.dimX-1:
            self.x += rnd.randint(-1,1)
        elif  self.x == 0:
            self.x += rnd.randint(0,1)
        else:
            self.x += rnd.randint(-1,0)

        if self.y != 0 and self.y != self.map.dimY-1:
                self.y += rnd.randint(-1,1)
        elif  self.y == 0:
            self.y += rnd.randint(0,1)
        else:
            self.y += rnd.randint(-1,0)

        self.map.updateOnIt(self.x,self.y,1,self)





    def die(self):
        self.map.updateOnIt(self.x,self.y,0,self)
        self.map.removeAnimal(self)