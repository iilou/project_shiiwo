import pygame 
import sys
from graph import *
from helpers import delta_2d_pos, toVector2
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

def draw(poly_list):
    uwu.fill(white)
    #print(str(poly_list))
    for poly in poly_list:
        pygame.draw.polygon(uwu, grey_dark_1, poly)

    for poly in poly_list:
        poly.append(poly[0])
        for i in range(len(poly) - 1):
            pygame.draw.line(uwu, black, poly[i], poly[i + 1])

    #pygame.draw.polygon(uwu, black, [(300, 300),(300,-300),(-300,-300),(-300,300)])

    pygame.display.flip()
draw(shiiwo.getImage())
clock = pygame.time.Clock()
cam_speed = 3
rot_speed = 0.0001
mouse_position = pygame.mouse.get_pos()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60)
    movement = [0,0,0]
    rotation = [0,0]
    input_keys = pygame.key.get_pressed()

    if input_keys[pygame.K_a]:
        movement[0] -= cam_speed * dt
    if input_keys[pygame.K_d]:
        movement[0] += cam_speed * dt
    if input_keys[pygame.K_w]:
        movement[1] += cam_speed * dt
    if input_keys[pygame.K_s]:
        movement[1] -= cam_speed * dt
    if input_keys[pygame.K_q]:
        movement[2] += cam_speed * dt  / 2
    if input_keys[pygame.K_e]:
        movement[2] -= cam_speed * dt  / 2

    if input_keys[pygame.K_LSHIFT]:
        cur_mouse_position = pygame.mouse.get_pos()
        delta_mouse_pos = delta_2d_pos(mouse_position, cur_mouse_position)
        mouse_position = cur_mouse_position

        rotation[0] = delta_mouse_pos[0] * rot_speed
        rotation[1] = delta_mouse_pos[1] * rot_speed

    
    shiiwo.update(movement, rotation)
    draw(shiiwo.getImage())


        
