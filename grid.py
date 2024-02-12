import pygame
import tile
import random
from perlin_noise import PerlinNoise




class Grid():
    """ Grid class, holds a 2D array of tiles as well as an array of all the cities for easy access."""

    def __init__(self,size:list[int],pixels_per_tile,WINDOW:pygame.Surface) -> None:
        grid_x,grid_y = size
        self.ppt = pixels_per_tile
        self.grid_x,self.grid_y = grid_x,grid_y
        self.WINDOW = WINDOW
        height_noise = PerlinNoise(2,random.randint(100,10000))
        fertility_noise = PerlinNoise(1,random.randint(100,10000))
        self.tile_list:list[list[tile.Tile]] = []
        for i in range(grid_x):
            self.tile_list.append([])
            for j in range(grid_y):
                height = int((height_noise([i/grid_x,j/grid_y])**2*300)) # Generate height (affects how tall (light brown to dark brown))
                fertility = int((fertility_noise([i/grid_x,j/grid_y])**2*1000)*100%3) # Generate fertility (affects how green tile is)
                print(height,fertility)
                new_tile = tile.Tile(i,j,height,fertility)
                self.tile_list[i].append(new_tile)

    def display(self):
        for tile_row in self.tile_list:
            for tile in tile_row:
                pygame.draw.rect(self.WINDOW,tile.color,pygame.Rect(tile.grid_x*self.ppt,tile.grid_y*self.ppt,(tile.grid_x+1)*self.ppt,(tile.grid_y+1)*self.ppt))

    def update(self):
        self.display()

    def getTile(self,grid_x,grid_y)->tile.Tile:
        return(self.tile_list[grid_x][grid_y])
