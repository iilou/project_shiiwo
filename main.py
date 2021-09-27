import pygame 
import sys
from helpers import toVector2
from world import World

pygame.init()

display_size = [1280, 720]

white = (255, 255, 255)
black = [0, 0, 0]

uwu = pygame.display.set_mode((1280,720))
uwu.fill(white)

shiiwo = World(display_size)

cube_dimensions = [[300,300,0], [300,-300,0],    [0,300,300],   [0,-300,300],   [0,300,-300],   [0,-300,-300],  [-300,300,0],   [-300,-300,0]]
shiiwo.addObject(cube_dimensions, "square")

#print(round([0.013, 0.147], 2))
print(str(shiiwo.objects[0].data))

poly_list = shiiwo.getImage()
#print(str(poly_list))
for poly in poly_list:
    pygame.draw.polygon(uwu, black, poly)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
