from perlin_noise import PerlinNoise
import random
import pygame

pygame.init()


WINDOW = pygame.display.set_mode((512,512))

new_noise = PerlinNoise(1,random.randint(100,10000))


for i in range(0,16,1):
    for j in range(0,16,1):
        color = [abs(int(100*new_noise([i/10,j/10]))),abs(int(100*new_noise([i/10,j/10]))),abs(int(100*new_noise([i/10,j/10])))]
        pygame.draw.rect(WINDOW,color,[i*32,j*32,(i+1)*32,(j+1)*32])
        print(new_noise([i/10,j/10]))

pygame.display.update()
game_running = True
while game_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()