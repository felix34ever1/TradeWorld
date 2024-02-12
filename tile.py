import pygame

class Tile():
    """Tile class, holds data about the smallest space on the map."""

    def __init__(self,grid_x,grid_y,height:int,fertility:int) -> None:
        self.grid_x:int = grid_x
        self.grid_y:int = grid_y
        self.fertility:int = fertility
        self.height:int = height
        minerals:int
        occupant = None
        self.color:list[int] = [0,0,0]
        height_color:pygame.Color = pygame.Color(height*2,height*2+1,height*2) # As value becomes more tall, red approaches green and blue approaches green, green stays same
        if height < 20:
            height_color+=pygame.Color(10,10,50+height)
        else:
            height_color+=pygame.Color(50,30*fertility,1)

        self.color = height_color
        print(self.color)

    def printData(self):
        print(f"Fertility:{self.fertility} Height:{self.height}")