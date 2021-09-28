import pygame 
import sys
from graph import *
from helpers import toVector2
from world import World

pygame.init()

display_size = [1280, 720]

white = (255, 255, 255)
grey_dark_1 = (80,80,80)
black = [0, 0, 0]

uwu = pygame.display.set_mode(display_size)
uwu.fill(white)

shiiwo = World(display_size)

cube_dimensions_1 = [Point_3(400,200,200), 
                    Point_3(800,200,200),    
                    Point_3(800,-200,200),   
                    Point_3(400,-200,200),   
                    Point_3(400,200,-200),   
                    Point_3(800,200,-200),  
                    Point_3(800,-200,-200),   
                    Point_3(400,-200,-200)]
cube_dimensions_2 = [Point_3(-200,200,200), 
                    Point_3(200,200,200),    
                    Point_3(200,-200,200),   
                    Point_3(-200,-200,200),   
                    Point_3(-200,200,-200),   
                    Point_3(200,200,-200),  
                    Point_3(200,-200,-200),   
                    Point_3(-200,-200,-200)]

shiiwo.addObject(cube_dimensions_1, "square")
shiiwo.addObject(cube_dimensions_2, "square")

#print(round([0.013, 0.147], 2))
#print(str(shiiwo.objects[0].data))

def draw():
    uwu.fill(white)
    poly_list = shiiwo.getImage()
    #print(str(poly_list))
    for poly in poly_list:
        pygame.draw.polygon(uwu, grey_dark_1, poly)

    for poly in poly_list:
        poly.append(poly[0])
        for i in range(len(poly) - 1):
            pygame.draw.line(uwu, black, poly[i], poly[i + 1])

    #pygame.draw.polygon(uwu, black, [(300, 300),(300,-300),(-300,-300),(-300,300)])

    pygame.display.flip()

draw()

clock = pygame.time.Clock()
cam_speed = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60)
    movement = [0,0,0]
    input_keys = pygame.key.get_pressed()

    if input_keys[pygame.K_a]:
        movement[0] -= cam_speed * dt
    if input_keys[pygame.K_d]:
        movement[0] += cam_speed * dt
    if input_keys[pygame.K_w]:
        movement[1] += cam_speed * dt
    if input_keys[pygame.K_s]:
        movement[1] -= cam_speed * dt
    if input_keys[pygame.K_SPACE]:
        movement[2] += cam_speed * dt
    if input_keys[pygame.K_LSHIFT]:
        movement[2] -= cam_speed * dt

    round(movement[0], 3)
    round(movement[1], 3)
    round(movement[2], 3)

    if not movement == [0,0,0]:
        shiiwo.camera.pos[0] += movement[0]
        shiiwo.camera.pos[1] += movement[1]
        shiiwo.camera.pos[2] += movement[2]
        draw()


        
