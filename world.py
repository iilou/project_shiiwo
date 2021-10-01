from objects import Object, Camera
from graph import *
from helpers import *

class World():
    def __init__(self, display_size):
        self.objects = []
        self.display_size = display_size
        self.start()

        self.camera = Camera(Point_3(0, 0, -1500), 70, [0,0,0], display_size)
        self.camera.start()

    def addObject(self, dim, type):
        self.objects.append(Object(dim, type))

    def start(self):
        #render stuff
        self.tl_vec = Vector_3()
        self.dot_h = Point_3(0,0,0)
        self.dot_v = Point_3(0,0,0)


    def render(self, position):
        self.tl_vec.init_points(position, self.camera.corner_topleft)   
        x = self.tl_vec.dot_raw(self.camera.h_vec)
        y = self.tl_vec.dot_raw(self.camera.v_vec)

        return [x, y]

#    def addCamera(self):

    def getImage(self):
        polygons = []

        for i in range(len(self.objects)):
            for face in self.objects[i].data:
                raw_position_list = self.camera.projection(face)
                conv_position_list = []

                for raw_position in raw_position_list:
                    #raw_position.print()
                    conv_position_list.append(self.render(raw_position))

                polygons.append(conv_position_list)

        return polygons
    
    def update(self, movement, rotation):
        self.camera.update(movement, rotation)
    

#camera = Camera([],[],0,[])
#shiiwo = World(camera)

#camera.pos = [5,5,5]
#shiiwo.camera.print()

#points = [[1, 5], [6, 2], [8, 8], [1, 9]]
#object = Object(points, False)
#shiiwo.addObject(object)
#shiiwo.objects[0].print()