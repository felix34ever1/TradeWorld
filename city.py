import pygame
import gameobject
import random

class City(gameobject.GameObject):
    """ Blah blah city class"""

    def __init__(self, WINDOW: pygame.Surface) -> None:
        super().__init__(WINDOW)
        self.food_production = 1
        self.mineral_extraction = 0
        self.population = 1
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        

    def update(self, time: int):
        self.color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

    def display(self,grid_x,grid_y,ppt):
        pygame.draw.circle(self.WINDOW,self.color,(grid_x*ppt+ppt//2,grid_y*ppt+ppt//2),ppt//2)