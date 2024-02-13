import pygame

class GameObject():
    """Base class for objects in the game, has the update and perMonth functions"""

    def __init__(self,WINDOW:pygame.Surface) -> None:
        self.WINDOW = WINDOW


    def display(self,grid_x,grid_y,ppt):
        pass

    def update(self,time:int,grid_x,grid_y,ppt):
        if time//30 == 0:
            self.perMonth()
        self.display()

    def perMonth(self):
        pass
