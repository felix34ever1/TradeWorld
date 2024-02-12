import pygame
import random
import grid

pygame.init()

DIMENSIONS = [150,150]
tiles_shown = [50,50]
PIXELS_PER_TILE = 10

WINDOW = pygame.display.set_mode((tiles_shown[0]*PIXELS_PER_TILE,tiles_shown[1]*PIXELS_PER_TILE))

world_grid = grid.Grid(DIMENSIONS,tiles_shown,PIXELS_PER_TILE,WINDOW)

is_playing = True

while is_playing:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            
            world_grid.getTile(mouse_x//PIXELS_PER_TILE,mouse_y//PIXELS_PER_TILE).printData()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                world_grid.changeOffset([0,-1])
            if event.key == pygame.K_s:
                world_grid.changeOffset([0,1])
            if event.key == pygame.K_a:
                world_grid.changeOffset([-1,0])
            if event.key == pygame.K_d:
                world_grid.changeOffset([1,0])


    world_grid.update()

    pygame.display.update()