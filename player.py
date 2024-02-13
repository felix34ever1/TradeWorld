import pygame
import gameobject
class Player(gameobject.GameObject):

    def __init__(self, WINDOW: pygame.Surface,starting_position:list[int]) -> None:
        super().__init__(WINDOW)
        self.inventory = None # To have an inventory object soon
        self.position = starting_position
        self.color = pygame.Color(255,255,0)

    def display(self,grid_x,grid_y,ppt):
        pygame.draw.rect(self.WINDOW,self.color,pygame.Rect(
            grid_x*ppt,
            grid_y*ppt,
            ppt,
            ppt
        ))

    def update(self, time: int,offset_x,offset_y,ppt):
        self.display(self.position[0]-offset_x,self.position[1]-offset_y,ppt)

