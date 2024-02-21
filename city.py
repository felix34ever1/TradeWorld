import pygame
import gameobject
import random
import building

class City(gameobject.GameObject):
    """ Blah blah city class"""

    def __init__(self, WINDOW: pygame.Surface) -> None:
        super().__init__(WINDOW)
        self.food_production = 1
        self.mineral_extraction = 0
        self.population = 1
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.buildings:list[building.Building] = []
        self.resources ={
            "food":0,
            "stone":0,
            "metal":0,
            "animal products":0,
            "clothing":0,
            "alcohol":0,
            "fabric":0

        }
        

    def update(self, time: int):
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

    def display(self,grid_x,grid_y,ppt):
        pygame.draw.circle(self.WINDOW,self.color,(grid_x*ppt+ppt//2,grid_y*ppt+ppt//2),ppt//2)