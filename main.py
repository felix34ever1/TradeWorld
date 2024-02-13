import pygame
import random
import grid
import city
import player

pygame.init()

DIMENSIONS = [100,100]
tiles_shown = [50,50]
PIXELS_PER_TILE = 10
offset_gradient = [0,0]


WINDOW = pygame.display.set_mode((tiles_shown[0]*PIXELS_PER_TILE,tiles_shown[1]*PIXELS_PER_TILE))

world_grid = grid.Grid(DIMENSIONS,tiles_shown,PIXELS_PER_TILE,WINDOW)

player_character = world_grid.player_character

cities_placed = 0
while cities_placed <10:
    xplace = random.randint(0,len(world_grid.tile_list)-1)
    yplace = random.randint(0,len(world_grid.tile_list[0])-1)
    if world_grid.tile_list[xplace][yplace].occupant == None and world_grid.tile_list[xplace][yplace].height>=2:
        world_grid.tile_list[xplace][yplace].occupant = city.City(WINDOW)
        cities_placed+=1

is_playing = True

while is_playing:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            
            grid_x,grid_y = mouse_x//PIXELS_PER_TILE,mouse_y//PIXELS_PER_TILE

            world_grid.getTile(grid_x,grid_y).printData()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                offset_gradient[1] = -1
            if event.key == pygame.K_s:
                offset_gradient[1] = 1
            if event.key == pygame.K_a:
                offset_gradient[0] = -1
            if event.key == pygame.K_d:
                offset_gradient[0] = 1

            if event.key == pygame.K_LEFT:
                world_grid.movePlayerByVector([-1,0])
            if event.key == pygame.K_RIGHT:
                world_grid.movePlayerByVector([1,0])
            if event.key == pygame.K_UP:
                world_grid.movePlayerByVector([0,-1])
            if event.key == pygame.K_DOWN:
                world_grid.movePlayerByVector([0,1])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                offset_gradient[1] = 0
            if event.key == pygame.K_s:
                offset_gradient[1] = 0
            if event.key == pygame.K_a:
                offset_gradient[0] = 0
            if event.key == pygame.K_d:
                offset_gradient[0] = 0 

    
    world_grid.changeOffset(offset_gradient)

    world_grid.update(0)

    pygame.display.update()