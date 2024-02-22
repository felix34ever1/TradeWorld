import pygame
import gameobject
import random
import building
import tile

class City(gameobject.GameObject):
    """ Blah blah city class"""

    def __init__(self, WINDOW: pygame.Surface,tile:tile.Tile) -> None:
        super().__init__(WINDOW)
        self.own_tile = tile
        self.food_production = 1
        self.food_used = 0
        self.mineral_extraction = 0
        self.population = 1
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.buildings:list[building.Building] = []
        self.resources ={
            "food":1,
            "wood":2,
            "stone":0,
            "metal":0,
            "animal products":0,
            "clothing":0,
            "alcohol":0,
            "fabric":0

        }
        

    def update(self, time: int):
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        
        # Resource management
        
        self.resources["food"]-=self.population
        for cur_building in self.buildings:
            cur_building.update(self)
        
        if self.resources["food"]>=self.population:
            self.population+=1
        elif self.resources["food"]<0:
            self.population-=1


        ### Survival needs

        # if food consumption>production 
        if self.food_production>self.food_used and self.population>self.resources["food"]:
            new_farm = building.Farmstead()
            # if can make farm do it
            if new_farm.check_costs(self):
                new_farm.construction(self)
                self.buildings.append(new_farm)
                self.food_used+=1
            # else make more lumber
            self.buildings.append(building.LumberMill())
        
        ### Expansion needs
        

        

    def display(self,grid_x,grid_y,ppt):
        pygame.draw.circle(self.WINDOW,self.color,(grid_x*ppt+ppt//2,grid_y*ppt+ppt//2),ppt//2)