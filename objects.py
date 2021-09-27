import math
from helpers import *

class Object():
    def __init__(self, data, type):
        self.data = data

        if type == "square": self.square()

    def square(self):
        points = []

        points.append([self.data[0], self.data[1], self.data[2], self.data[3]])
        points.append([self.data[0], self.data[4], self.data[5], self.data[1]])
        points.append([self.data[3], self.data[2], self.data[6], self.data[7]])
        points.append([self.data[0], self.data[4], self.data[7], self.data[3]])
        points.append([self.data[1], self.data[5], self.data[6], self.data[2]])
        points.append([self.data[4], self.data[5], self.data[6], self.data[7]])

        self.data = points

    def print(self):
        for i in self.data:
            print(i)

#square = Object([[1, 2, -1], [2, 3, 1], [8, -2, 3]], False)
#square.print()


class Camera():
    def __init__(self, pos, fov, rot, dim):
        self.pos = pos
        self.fov = fov
        self.rot = rot
        self.dim = dim
        
        self.point_screen = []
        self.point_focus = []
        self.screen_dimensions = dim

        self.screen_corners = [[],[],[],[]]
        self.screen_vec = []
        self.screen_plane = []

    def projection(self, face):
        polygon = []

        #print(face)

        for point in face:
            d_vec = [self.point_focus[0] - point[0], self.point_focus[1] - point[1], self.point_focus[2] - point[2]]

            polygon.append(vec_intersect_plane(self.screen_plane, d_vec, point))

            #print(str(d_vec))
            #print(t_val)

        return polygon

    def update(self):
        self.point_screen = self.pos
        self.screen_dimensions = self.dim

        wd = self.screen_dimensions[0]/2
        hd = self.screen_dimensions[1]/2

        self.screen_corners[0] = [self.point_screen[0] - wd, self.point_screen[1] + hd, self.point_screen[2]]
        self.screen_corners[1] = [self.point_screen[0] - wd, self.point_screen[1] - hd, self.point_screen[2]]
        self.screen_corners[2] = [self.point_screen[0] + wd, self.point_screen[1] + hd, self.point_screen[2]]
        self.screen_corners[3] = [self.point_screen[0] + wd, self.point_screen[1] - hd, self.point_screen[2]]

        delta_z = wd * math.tan(math.radians(self.fov/2))

        #print(delta_z)

        self.point_focus = [self.point_screen[0], self.point_screen[1], self.point_screen[2] - delta_z]
        self.screen_vec = vec_make(self.point_screen, self.point_focus)

        self.screen_plane = self.screen_vec
        self.screen_plane.append(self.point_screen[0] * self.screen_vec[0] + self.point_screen[1] * self.screen_vec[1] + self.point_screen[2] * self.screen_vec[2])
        
        print(str(self.screen_vec))
        print(str(self.point_focus))
        print(str(self.screen_plane), "\n")


    def print(self):
        print("")