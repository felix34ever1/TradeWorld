import pygame
import random
import grid

pygame.init()

DIMENSIONS = [100,100]
PIXELS_PER_TILE = 10

WINDOW = pygame.display.set_mode((DIMENSIONS[0]*PIXELS_PER_TILE,DIMENSIONS[1]*PIXELS_PER_TILE))

world_grid = grid.Grid(DIMENSIONS,PIXELS_PER_TILE,WINDOW)

is_playing = True

while is_playing:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            world_grid.getTile(mouse_x//PIXELS_PER_TILE,mouse_y//32).printData()

    world_grid.update()

    pygame.display.update()