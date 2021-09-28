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

    def projection(self, face):
        polygon = []

        #print(face)

        for point in face:
            point_to_focus_eq = linearequation_make(point, self.point_focus)
            point_to_focus_int = self.screen_plane.intersect_linearequation(point_to_focus_eq)

            polygon.append(point_to_focus_int)

        return polygon

    def update(self):
        self.point_screen = self.pos
        self.screen_dimensions = self.dim

        wd = self.screen_dimensions[0]/2
        hd = self.screen_dimensions[1]/2

        delta_z = wd * math.tan(math.radians(self.fov/2))

        self.corner_topleft = self.point_screen
        self.corner_topleft.x -= wd
        self.corner_topleft.y += hd

        self.h_screen_eq = linearequation_make_vec(vec_make_raw(1, 0, 0), self.corner_topleft)
        self.v_screen_eq = linearequation_make_vec(vec_make_raw(0, -1, 0), self.corner_topleft)
        #print(delta_z)

        self.point_focus = self.point_screen
        self.point_focus.z -= delta_z
        self.screen_vec = vec_make_points(self.point_screen, self.point_focus)

        self.screen_plane = plane_make_vecnpoint(self.screen_vec, self.point_screen)
        
        print(str(self.screen_vec))
        print(str(self.point_focus))
        print(str(self.screen_plane), "\n")


    def print(self):
        print("")