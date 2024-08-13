class plant:
    
    def __init__(self,species,x,y,mapObj,nutirtionalValue):
        self.species = species
        self.x = x
        self.y = y
        self.map = mapObj

        self.nutritionalValue = nutirtionalValue
        
        self.stage = 3

    def grow(self):
        self.stage += 1

        if self.stage > 3:
            self.map.updateType(self.x,self.y,self)
            self.map.growing.remove(self)

    def eaten(self):
        self.stage = 0
        self.map.growing.add(self)
        self.map.updateType(self.x, self.y,plant("grass",self.x,self.y,self.map,0.75))
            