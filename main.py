import pygame
import random
import grid
import city
import player

pygame.init()

DIMENSIONS = [90,90]
tiles_shown = [30,30]
PIXELS_PER_TILE = 24
offset_gradient = [0,0]
time = 0

game_font = pygame.font.Font("C&C Red Alert [INET].ttf",20)


WINDOW = pygame.display.set_mode((tiles_shown[0]*PIXELS_PER_TILE,tiles_shown[1]*PIXELS_PER_TILE))

world_grid = grid.Grid(DIMENSIONS,tiles_shown,PIXELS_PER_TILE,WINDOW)

player_character = world_grid.player_character

cities_placed = 0
while cities_placed <10:
    xplace = random.randint(0,len(world_grid.tile_list)-1)
    yplace = random.randint(0,len(world_grid.tile_list[0])-1)
    if world_grid.tile_list[xplace][yplace].occupant == None and world_grid.tile_list[xplace][yplace].height>=2:
        world_grid.tile_list[xplace][yplace].occupant = city.City(WINDOW,world_grid.tile_list[xplace][yplace])
        cities_placed+=1

is_playing = True

state_world = True
state_city_menu = False
just_switched = False

while is_playing:

    events = pygame.event.get()
    just_switched = False
    for event in events:
        if event.type == pygame.QUIT:
            is_playing = False
        
        if state_world:
        
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
                if event.key == pygame.K_SPACE and not just_switched:
                    if world_grid.isPlayerAtCity():
                        offset_gradient = [0,0]
                        state_world = False
                        state_city_menu = True
                        just_switched = True
                    

                time_taken = 0
                if event.key == pygame.K_LEFT:
                    time_taken+=world_grid.movePlayerByVector([-1,0])
                if event.key == pygame.K_RIGHT:
                    time_taken+=world_grid.movePlayerByVector([1,0])
                if event.key == pygame.K_UP:
                    time_taken+=world_grid.movePlayerByVector([0,-1])
                if event.key == pygame.K_DOWN:
                    time_taken+=world_grid.movePlayerByVector([0,1])

                time+=time_taken

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    offset_gradient[1] = 0
                if event.key == pygame.K_s:
                    offset_gradient[1] = 0
                if event.key == pygame.K_a:
                    offset_gradient[0] = 0
                if event.key == pygame.K_d:
                    offset_gradient[0] = 0 

        if state_city_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not just_switched:
                    state_world = True
                    state_city_menu = False
                    just_switched = True


    if state_world:
        world_grid.changeOffset(offset_gradient)

        world_grid.update(time)
        world_grid.display()
    if state_city_menu:
        world_grid.displayCity()

    WINDOW.blit(game_font.render(f"Day: {time}",False,(255,255,255)),[20,20])

    pygame.display.update()