
import map
import animal 
import time
import plant
import random as r

SMALL_HERBIVORE_DIET = set(['shrub'])
SMALL_CARNIVORE_DIET = set(["rabbit"])

dimX = 10
dimY = 10
newMap = map.map(dimX,dimY)

newMap.printMap()

genes  = {'mutationRate': 0.4, 'hungerThreshold': 5, 'matingCoolDown':10, 'viewingDistance':3, 'hunger': 15}


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)


#fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
#newMap.animals.add(fox)
#fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
#newMap.animals.add(fox)
#fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,25)
#newMap.animals.add(fox)


for _ in range(50):

    
    for animal in list(newMap.animals):
        animal.turn()
    
    for growing in list(newMap.growing):
        growing.grow()

    newMap.printMap()

    time.sleep(0.75)

