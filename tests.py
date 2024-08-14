
import map
import animal 
import time
import plant
import random as r

SMALL_HERBIVORE_DIET = set(['shrub'])
SMALL_CARNIVORE_DIET = set(["rabbit"])

dimX = 14
dimY = 14
newMap = map.map(dimX,dimY)

newMap.printMap()

genes  = {'mutationRate': 0.5, 'hungerThreshold': 5, 'matingCoolDown':5, 'viewingDistance':3, 'hunger': 15}


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)


rabbit = animal.herbivore("rabbit",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap, SMALL_HERBIVORE_DIET,genes)
newMap.animals.add(rabbit)

genes  = {'mutationRate': 0.1, 'hungerThreshold': 7, 'matingCoolDown':8, 'viewingDistance':5, 'hunger': 15}

fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,genes)
newMap.animals.add(fox)
fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,genes)
newMap.animals.add(fox)
fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,genes)
newMap.animals.add(fox)

fox = animal.carnivore("fox",r.randint(0,dimX-1),r.randint(0,dimY-1),newMap,SMALL_CARNIVORE_DIET,genes)
newMap.animals.add(fox)


for _ in range(75):
    
    for animal in list(newMap.animals):
        animal.turn()
    
    for growing in list(newMap.growing):
        growing.grow()

    newMap.printMap()

    #time.sleep(0.75)

foxGenes = [[] for _ in range(len(genes))]

rabbitGenes = [[] for _ in range(len(genes))]

for animal in list(newMap.animals):
    vals = list(animal.genes.values())
    if animal.species == "fox":
        for i in range(len(vals)):
            foxGenes[i].append(vals[i])
            
    else:
        for i in range(len(vals)):
            rabbitGenes[i].append(vals[i])

print("Foxes")

for i in foxGenes:
    if i:
        print(sum(i) / len(i))
    else:
        print(0)
print("Rabbits")
for i in rabbitGenes:
    print(sum(i) / len(i))
