import pygame

class Building():
    def __init__(self) -> None:
        self.image = pygame.image.load("images/yellowsquare.png")

    def update(self,target_city)->None: # Ran at end of month
        target_city:city.City = target_city 
    
    def check_costs(self,target_city)->bool: # Ran to check if the building can be built
        target_city:city.City = target_city
        return False
    
    def construction(self,target_city)->None: # Ran when the building is actually constructed to take away resources from the city
        target_city:city.City = target_city

class Farmstead(Building):
    def __init__(self) -> None:
        super().__init__()
        self.production = 1
    
    def update(self,target_city)->None: # Ran at end of month
        target_city:city.City = target_city
        target_city.resources["food"]+=1
    
    def check_costs(self,target_city)->bool: # Ran to check if the building can be built
        target_city:city.City = target_city
        if target_city.resources["wood"] > 0: 
            return True
        else:
            return False
    
    def construction(self,target_city)->None: # Ran when the building is actually constructed to take away resources from the city
        target_city:city.City = target_city
        target_city.resources["wood"] -= 1
        

class LumberMill(Building):
    def __init__(self) -> None:
        super().__init__()
        self.production = 1
    
    def update(self,target_city)->None: # Ran at end of month
        target_city:city.City = target_city
        target_city.resources["wood"]+=self.production
    
    def check_costs(self,target_city)->bool: # Ran to check if the building can be built
        target_city:city.City = target_city
        return True
    
    def construction(self,target_city)->None: # Ran when the building is actually constructed to take away resources from the city
        target_city:city.City = target_city
        


import city