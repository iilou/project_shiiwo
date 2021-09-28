from objects import Object, Camera
from graph import *
from helpers import vec_make_points, vec_subtract, vec_cross, length_3

class World():
    def __init__(self, display_size):
        self.objects = []
        self.display_size = display_size

        self.camera = Camera(Point_3(0, 0, -1500), 70, [0,0,0], display_size)

    def addObject(self, dim, type):
        self.objects.append(Object(dim, type))

#    def addCamera(self):

    def getImage(self):
        self.camera.update()

        polygons = []

        for i in range(len(self.objects)):
            for face in self.objects[i].data:
                raw_position_list = self.camera.projection(face)
                conv_position_list = []
                #print(str(raw_position_list))
                
                #screen_size = [length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[1])), length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[2]))]
                #print(str(screen_size))

                for raw_position in raw_position_list:
                    vertical_eq = self.camera.v_screen_eq
                    vertical_eq.set_pos(raw_position)

                    horizontal_eq = self.camera.h_screen_eq
                    horizontal_eq.set_pos(raw_position)

                    h_int = vertical_eq.intersect_linearequation(self.camera.h_screen_eq)
                    v_int = vertical_eq.intersect_linearequation(self.camera.v_screen_eq)

                    conv_pos = [0,0]
                    h_vec = vec_make_points(h_int, self.camera.corner_topleft)
                    h_direction = 1
                    if h_vec.opposite(self.camera.h_screen_eq.get_vec()): h_direction = -1
                    conv_pos[0] = h_direction * length_3(h_vec)

                    v_vec = vec_make_points(v_int, self.camera.corner_topleft)
                    v_direction = 1
                    if v_vec.opposite(self.camera.v_screen_eq.get_vec()): v_direction = -1
                    conv_pos[1] = v_direction * length_3(v_vec)

                    conv_position_list.append(conv_pos)

                    
                # print(face)
                # print(raw_position_list)
                # print(conv_position_list)
                # print("")

                polygons.append(conv_position_list)

        return polygons
    

#camera = Camera([],[],0,[])
#shiiwo = World(camera)

#camera.pos = [5,5,5]
#shiiwo.camera.print()

#points = [[1, 5], [6, 2], [8, 8], [1, 9]]
#object = Object(points, False)
#shiiwo.addObject(object)
#shiiwo.objects[0].print()