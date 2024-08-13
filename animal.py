import random as rnd
import animal

SMALL_HERBIVORE_DIET = set(['shrub','grass'])
SMALL_CARNIVORE_DIET = set(["rabbit"])

class animal:
    def __init__(self,species,x,y,mapObj, diet,weight):
        self.species = species
        self.id = 1
        
        self.x = x
        self.y = y
        
        self.weight = weight
        self.hunger = 10
        self.diet = diet
        self.cooldown = 0
        self.map = mapObj


        self.map.updateOnIt(x,y,1,self)

    def turn(self):
        
        self.move()
        self.hunger -= 1
        self.cooldown -= 1
        self.eat()
        
        if self.hunger > 5 and self.cooldown <= 0:
            for onIt in self.map.getOnIt(self.x,self.y):
                if onIt != self and onIt.species == self.species:
                    self.mate(onIt)
                    break


        if self.hunger < 0:
            self.die()






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
        print(self.species, "died")





class carnivore(animal):
    def __init__(self, species, x, y, mapObj,diet,weight):

        self.nutritionalValue = 0.1 * weight

        super().__init__(species, x, y, mapObj,diet,weight)

    
    def eat(self):
        curOnIt = self.map.getOnIt(self.x,self.y)
        
        for onTile in curOnIt:
            if onTile != self and onTile.species in self.diet:
                self.hunger += onTile.nutritionalValue
                onTile.die()
                print(self.species, "ate", onTile.species)
                break

    def mate(self,other):
        self.hunger -= 2
        other.hunger -= 2
        self.cooldown = 10
        other.cooldown = 10

        newAnimal = make("C",self.species,self.x,self.y,self.map, self.diet, self.weight)
        print(self.species, 'mated with', other.species)
        self.map.addAnimal(newAnimal)    

class herbivore(animal):
    def __init__(self, species, x, y, mapObj,diet,weight):
        self.nutritionalValue = weight

        super().__init__(species, x, y, mapObj,diet,weight)
        
    def eat(self):
        curType = self.map.getType(self.x,self.y)
        if curType.species in self.diet:
            self.hunger += curType.nutritionalValue
            
    def mate(self,other):
        self.hunger -= 2
        other.hunger -= 2
        self.cooldown = 10
        other.cooldown = 10

        newAnimal = make("H",self.species,self.x,self.y,self.map, self.diet, self.weight)
        print(self.species, 'mated with', other.species)
        self.map.addAnimal(newAnimal)

class omivore(animal): 
    def __init__(self, species, x, y, mapObj,diet,weight):
        
        self.nutritionalValue = weight * 0.75
        
        super().__init__(species, x, y, mapObj,diet,weight)



def make(type,species,x,y,map,diet,weight):
    if type == 'H':
        return herbivore(species,x,y,map,diet,weight)
    elif type == 'C':
        return carnivore(species,x,y,map,diet,weight)
