import random as rnd
import animal
import plant 
SMALL_HERBIVORE_DIET = set(['shrub'])
SMALL_CARNIVORE_DIET = set(["rabbit"])

class animal:
    def __init__(self,species,x,y,mapObj, diet,genes):
        self.species = species
        self.id = 1
        
        self.x = x
        self.y = y
        
        self.genes = genes
        self.viewingDistance = int(genes['viewingDistance'])
        self.hungerThreshold = int(genes['hungerThreshold'])
        self.mutationRate = genes['mutationRate']
        self.matingCoolDown = int(genes['matingCoolDown'])
        self.hunger = int(genes['hunger'])
        
        self.weight = self.hunger * 1.5
        
        self.diet = diet
        self.cooldown = self.matingCoolDown
        self.map = mapObj

        self.seekingFood = None
        self.seekingMate = None
        self.map.updateOnIt(x,y,1,self)

    def turn(self):
        self.hunger -= 1
        self.cooldown -= 1
        
        self.move()

        self.eat()
        
        if self.hunger > self.hungerThreshold and self.cooldown <= 0:
            for onIt in self.map.getOnIt(self.x,self.y):
                if onIt != self and onIt.species == self.species:
                    self.mate(onIt)
                    break


        if self.hunger < 0:
            self.die()

    def findMate(self):
        minDist = (float('inf'),float('inf'))
        for dy in range(-self.viewingDistance,self.viewingDistance + 1):
            for dx in range(-self.viewingDistance,self.viewingDistance + 1):
                x = self.x + dx
                y = self.y + dy
                if self.map.inRange(x,y):
                    for onIt in self.map.getOnIt(x,y):
                        if onIt != self and onIt.species == self.species:             
                            if abs(dx) < abs(minDist[0]) or abs(dy) < abs(minDist[1]):
                                minDist = x,y
                            break
              
        return minDist
    


    
    def randomMove(self):
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




    def seek(self,seekee):

        if seekee[0] == self.x and seekee[1] == self.y:
            seekee = None
            return

        self.map.updateOnIt(self.x,self.y,0,self)        
        if seekee[0] != self.x:
            distX = seekee[0] - self.x
            self.x += distX//abs(distX)
        
        if seekee[1] != self.y:
            distY = seekee[1] - self.y
            self.y += distY//abs(distY)
        

        
        self.map.updateOnIt(self.x,self.y,1,self)


    def die(self):
        self.map.updateOnIt(self.x,self.y,0,self)
        self.map.removeAnimal(self)
        #print(self.species, "died")


    def passGenes(self,mother,father):
        newGenes = {}
        for i in mother.genes:
            r = rnd.random()
            if r > 0.5:
                passer = mother
            else:
                passer = father

            
            newGenes[i] = passer.genes[i] + ((rnd.random()-0.5)*(passer.genes[i]* passer.mutationRate))
        return newGenes


class carnivore(animal):
    def __init__(self, species, x, y, mapObj,diet,genes):
        super().__init__(species, x, y, mapObj,diet,genes)

        self.nutritionalValue = 0.1 * self.weight


    
    def eat(self):
        curOnIt = self.map.getOnIt(self.x,self.y)
        
        for onTile in curOnIt:
            if onTile != self and onTile.species in self.diet:
                self.hunger += onTile.nutritionalValue
                onTile.die()
                #print(self.species, "ate", onTile.species)
                break

    def mate(self,other):
        self.hunger -= 2
        other.hunger -= 2
        self.cooldown = self.matingCoolDown
        other.cooldown = other.matingCoolDown

        newGenes = self.passGenes(self,other)
        
        newAnimal = make("C",self.species,self.x,self.y,self.map, self.diet, newGenes)
        #print(self.species, 'mated with', other.species)
        self.map.addAnimal(newAnimal)    

    
    def findFood(self):
        minDist = (float('inf'),float('inf'))
        for dy in range(-self.viewingDistance,self.viewingDistance + 1):
            for dx in range(-self.viewingDistance,self.viewingDistance + 1):
                x = self.x + dx
                y = self.y + dy
                if self.map.inRange(x,y):
                    for onIt in self.map.getOnIt(x,y):
                        if onIt != self and onIt.species in self.diet:             
                            if abs(dx) < abs(minDist[0]) or abs(dy) < abs(minDist[1]):
                                minDist = x,y
                            

        return minDist
    
    def move(self):

        if self.hunger > self.hungerThreshold and self.cooldown <= 0 and self.seekingMate: 
            x,y = self.findMate()
            if x == float('inf'):
                self.seekingMate = None 
                self.randomMove()
            else:
                self.seekingMate = (x,y)
                self.seek(self.seekingMate)
            return
        

        if self.seekingFood:
            x,y = self.findFood()
            if x == float('inf'):
                self.seekingMate = None 
                self.randomMove()
            else:
                self.seekingMate = (x,y)
                self.seek(self.seekingFood)
            return
        
        if self.hunger < self.hungerThreshold:
            x,y = self.findFood()

            if x == float('inf'):
                self.seekingFood = None 
                self.randomMove()
            else:
                self.seekingFood = (x,y)
                self.seek(self.seekingFood)

        elif self.hunger > int(self.hungerThreshold * 1.5) and self.cooldown <= 0:
            x,y = self.findMate()

            if x == float('inf'):
                self.seekingMate = None 
                self.randomMove()
            else:
                self.seekingMate = (x,y)
                self.seek(self.seekingMate)

        else:
            self.seekingFood = None
            self.seekingMate = None 
            self.randomMove()    


class herbivore(animal):
    def __init__(self, species, x, y, mapObj,diet,genes):

        super().__init__(species, x, y, mapObj,diet,genes)

        self.nutritionalValue = 2 * self.weight

        
    def eat(self):
        curType = self.map.getType(self.x,self.y)
        if curType.species in self.diet:
            self.hunger += curType.nutritionalValue
            curType.eaten()

    def mate(self,other):
        self.hunger -= 2
        other.hunger -= 2
        self.cooldown = self.matingCoolDown
        other.cooldown = other.matingCoolDown

        newGenes = self.passGenes(self,other)

        newAnimal = make("H",self.species,self.x,self.y,self.map, self.diet, newGenes)
        #print(self.species, 'mated with', other.species)
        self.map.addAnimal(newAnimal)

        
    def findFood(self):
        minDist = (float('inf'),float('inf'))
        for dy in range(-self.viewingDistance,self.viewingDistance + 1):
            for dx in range(-self.viewingDistance,self.viewingDistance + 1):
                x = self.x + dx
                y = self.y + dy
                if self.map.inRange(x,y) and self.map.getType(x,y).species in self.diet:
                    if abs(dx) < abs(minDist[0]) or abs(dy) < abs(minDist[1]):
                        minDist = x,y
        return minDist
    

    def move(self):

        if self.hunger > self.hungerThreshold and self.cooldown <= 0 and self.seekingMate: 
            x,y = self.findMate()
            if x == float('inf'):
                self.seekingMate = None 
                self.randomMove()
            else:
                self.seekingMate = (x,y)
                self.seek(self.seekingMate)
            return
        

        if self.seekingFood:
            self.seek(self.seekingFood)
            return
        
        if self.hunger < self.hungerThreshold:
            x,y = self.findFood()

            if x == float('inf'):
                self.seekingFood = None 
                self.randomMove()
            else:
                self.seekingFood = (x,y)
                self.seek(self.seekingFood)

        elif self.hunger > int(self.hungerThreshold * 1.5) and self.cooldown <= 0:
            x,y = self.findMate()

            if x == float('inf'):
                self.seekingMate = None 
                self.randomMove()
            else:
                self.seekingMate = (x,y)
                self.seek(self.seekingMate)

        else:
            self.seekingFood = None
            self.seekingMate = None 
            self.randomMove()

class omivore(animal): 
    def __init__(self, species, x, y, mapObj,diet,weight):
        
        self.nutritionalValue = weight * 0.75
        
        super().__init__(species, x, y, mapObj,diet,weight)



def make(type,species,x,y,map,diet,weight):
    if type == 'H':
        return herbivore(species,x,y,map,diet,weight)
    elif type == 'C':
        return carnivore(species,x,y,map,diet,weight)
