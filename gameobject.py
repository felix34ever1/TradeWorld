import pygame

class GameObject():
    """Base class for objects in the game, has the update and perMonth functions"""

    def __init__(self,WINDOW:pygame.Surface) -> None:
        self.WINDOW = WINDOW


    def display(self):
        pass

    def update(self,time:int):
        if time//30 == 0:
            self.perMonth()
        self.display()

    def perMonth(self):
        pass
