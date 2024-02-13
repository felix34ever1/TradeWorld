import pygame
import tile
import random
import city
import player
from perlin_noise import PerlinNoise




class Grid():
    """ Grid class, holds a 2D array of tiles as well as an array of all the cities for easy access."""

    def __init__(self,map_size:list[int],screen_size:list[int],pixels_per_tile,WINDOW:pygame.Surface) -> None:
        grid_x,grid_y = map_size
        self.screen_size = screen_size
        self.offset:list[int] = [0,0]
        self.ppt = pixels_per_tile
        self.grid_x,self.grid_y = grid_x,grid_y
        self.time = 0 # Days passed
        self.WINDOW = WINDOW
        height_noise = PerlinNoise(2,random.randint(100,10000))
        fertility_noise = PerlinNoise(1,random.randint(100,10000))
        self.tile_list:list[list[tile.Tile]] = []
        for i in range(grid_x):
            self.tile_list.append([])
            for j in range(grid_y):
                height = int((height_noise([i/grid_x,j/grid_y])**2*300)) # Generate height (affects how tall (light brown to dark brown))
                fertility = int((fertility_noise([i/grid_x,j/grid_y])**2*1000)*100%4) # Generate fertility (affects how green tile is)
                print(height,fertility)
                new_tile = tile.Tile(i,j,height,fertility,self.WINDOW)
                self.tile_list[i].append(new_tile)

        self.player_character = player.Player(self.WINDOW,[5,5])

    def display(self):
        for i in range(self.screen_size[0]):
            for j in range(self.screen_size[1]):
                tile_used = self.tile_list[i+self.offset[0]][j+self.offset[1]]
                pygame.draw.rect(self.WINDOW,
                                 tile_used.color,
                                 pygame.Rect(i*self.ppt,j*self.ppt,self.ppt,self.ppt))
                tile_used.update(self.time)
                if tile_used.occupant != None:
                    if type(tile_used.occupant) == city.City:
                        tile_used.occupant.update(self.time,tile_used.grid_x-self.offset[0],tile_used.grid_y-self.offset[1],self.ppt)        

    def update(self,time):
        self.time = time
        self.display()
        self.player_character.update(time,self.offset[0],self.offset[1],self.ppt)

        

    def changeOffset(self,offset_vector:list[int]):
        """ Input a list of 2 elements of -1,0 or +1 each. These represent the screen moving left right up down."""
        if (offset_vector[0]>0 and self.offset[0]<self.grid_x-self.screen_size[0]) or (offset_vector[0]<0 and self.offset[0]>0):
            self.offset[0]+=offset_vector[0]
        if (offset_vector[1]>0 and self.offset[1]<self.grid_y-self.screen_size[1]) or (offset_vector[1]<0 and self.offset[1]>0):
            self.offset[1]+=offset_vector[1]
        
    def movePlayerByVector(self,move_vector:list[int]):
        """ Input a list of 2 elements of -1,0 or +1 each. These represent the player moving left right up down."""
        if (move_vector[0]>0 and self.player_character.position[0]<self.grid_x) or (move_vector[0]<0 and self.player_character.position[0]>0):
            self.player_character.position[0]+=move_vector[0]
        if (move_vector[1]>0 and self.player_character.position[1]<self.grid_y) or (move_vector[1]<0 and self.player_character.position[1]>0):
            self.player_character.position[1]+=move_vector[1]

    def getTile(self,grid_x,grid_y)->tile.Tile:
        return(self.tile_list[grid_x][grid_y])
