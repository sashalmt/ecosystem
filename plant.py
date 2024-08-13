class plant:
    
    def __init__(self,species,x,y,mapObj,nutirtionalValue):
        self.species = species
        self.x = x
        self.y = y
        self.map = mapObj

        self.nutritionalValue = nutirtionalValue
        
        self.stage = 3