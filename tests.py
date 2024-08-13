
import map
import animal 
import time
import plant


newMap = map.map(10,10)

newMap.printMap()

rabbit = animal.animal("Rabbit",2,2,newMap)

newMap.animals.add(rabbit)

fox = animal.animal("Fox",3,2,newMap)
newMap.animals.add(fox)

for _ in range(5):

    
    for animal in list(newMap.animals):
        animal.turn()
    
    newMap.printMap()

    time.sleep(2)

