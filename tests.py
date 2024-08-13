
import map
import animal 
import time
import plant
import random as r

SMALL_HERBIVORE_DIET = set(['shrub','grass'])
SMALL_CARNIVORE_DIET = set(["rabbit"])

dimX = 20
dimY = 20
newMap = map.map(dimX,dimY)

newMap.printMap()

rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,15)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,15)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,15)
newMap.animals.add(rabbit)


fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
newMap.animals.add(fox)
fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
newMap.animals.add(fox)
fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
newMap.animals.add(fox)
for _ in range(20):

    
    for animal in list(newMap.animals):
        animal.turn()
    
    newMap.printMap()

    time.sleep(0.75)

