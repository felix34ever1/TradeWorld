import pygame
import gameobject
class Player(gameobject.GameObject):

    def __init__(self, WINDOW: pygame.Surface,starting_position:list[int]) -> None:
        super().__init__(WINDOW)
        self.inventory = None # To have an inventory object soon
        self.position = starting_position
        self.color = pygame.Color(255,255,0)

    def display(self,offset_x,offset_y,ppt):
        pygame.draw.rect(self.WINDOW,self.color,pygame.Rect(
            (self.position[0]-offset_x)*ppt,
            (self.position[1]-offset_y)*ppt,
            ppt,
            ppt
        ))

    def update(self, time: int):
        pass
