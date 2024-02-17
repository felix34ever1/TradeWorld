import pygame
import gameobject

class Tile(gameobject.GameObject):
    """Tile class, holds data about the smallest space on the map."""

    def __init__(self,grid_x,grid_y,height:int,fertility:int,WINDOW:pygame.surface) -> None:
        super().__init__(WINDOW)
        self.grid_x:int = grid_x
        self.grid_y:int = grid_y
        self.fertility:int = fertility
        self.height:int = height
        self.minerals:int = height//20
        self.occupant:gameobject.GameObject = None
        self.color:list[int] = [0,0,0]
        height_color:pygame.Color = pygame.Color(height,height,height)
        self.movement_difficulty = self.height//10 + 1#The cost of the movement in days that it takes to travel
        if self.height>40 and self.fertility>0:
            self.fertility-=1
        if self.height<5 and self.fertility<4:
            self.fertility+=1
        if self.height < 2:
            height_color+=pygame.Color(10,10,50+self.height)
            self.movement_difficulty = 10
        else:
            height_color+=pygame.Color(50,30*self.fertility,1)

        self.color = height_color
        print(self.color)

    def printData(self):
        print(f"Fertility:{self.fertility} Height:{self.height}")
        
    def update(self, time: int,grid_x,grid_y,ppt):
        if self.occupant!= None:
            self.occupant.update(time)

    def display(self,grid_x,grid_y,ppt):
        if self.occupant!=None:
            self.occupant.display(grid_x,grid_y,ppt)