from objects import Object, Camera
from helpers import vec_subtract, vec_cross, length_3

class World():
    def __init__(self, display_size):
        self.objects = []
        self.display_size = display_size

        self.camera = Camera([0, 0, -1500], 70, [0,0,0], display_size)

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

                screen_size = [length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[1])), length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[2]))]
                #print(str(screen_size))

                for raw_position in raw_position_list:
                    #print(raw_position)
                    #print(str(self.camera.screen_corners))
                    d_h = length_3(vec_cross(vec_subtract(raw_position, self.camera.screen_corners[1]), vec_subtract(raw_position, self.camera.screen_corners[0]))) / length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[1]))
                    d_v = length_3(vec_cross(vec_subtract(raw_position, self.camera.screen_corners[2]), vec_subtract(raw_position, self.camera.screen_corners[0]))) / length_3(vec_subtract(self.camera.screen_corners[0], self.camera.screen_corners[2]))
                    #print(d_h, d_v)
                    x_pos = (d_h / screen_size[0]) * self.display_size[0]
                    y_pos = (d_v / screen_size[1]) * self.display_size[1]


                    conv_position_list.append([d_h, d_v])
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