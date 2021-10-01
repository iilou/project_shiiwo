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

    def start(self):
        self.point_screen = self.pos
        self.screen_dimensions = self.dim

        wd = self.screen_dimensions[0]/2
        hd = self.screen_dimensions[1]/2

        delta_z = wd * math.tan(math.radians(self.fov/2))

        self.corner_topleft = Point_3(self.point_screen.x - wd, self.point_screen.y + hd, self.point_screen.z)

        self.h_vec = vec_make_raw(1,0,0)
        self.v_vec = vec_make_raw(0,-1,0)
        #print(delta_z)

        self.point_focus = self.point_screen.get_copy()
        self.point_focus.z -= delta_z
        #self.point_focus.print()

        self.screen_vec = vec_make_points(self.point_screen, self.point_focus)
        self.screen_vec.unit_vec()

        self.screen_plane = plane_make_vecnpoint(self.screen_vec, self.point_screen)

        self.point_to_focus_equation = Linear_Equation()
        self.point_to_focus_equation.init_raw(0,0,0,0,0,0)
        self.poi = Point_3(0,0,0)

        # self.point_screen.print()
        # self.screen_plane.print()
        # self.screen_vec.print()
        # self.h_screen_eq.print()
        # self.v_screen_eq.print()
        # self.point_focus.print()
        # print("")

    def update(self, movement, rotation):
        #wd = self.screen_dimensions[0]/2
        #hd = self.screen_dimensions[1]/2


        if not movement == [0,0,0]:
            self.corner_topleft.move(movement)
            self.point_screen.move(movement)
            #self.point_screen.print()
            self.point_focus.move(movement)

            self.screen_plane.set_d(self.point_screen)
            self.screen_plane.d

        if not rotation == [0,0]:
            self.point_screen.rot_xz(self.point_focus, rotation[0])
            self.corner_topleft.rot_xz(self.point_focus, rotation[0])

            self.screen_vec.rot_xz(self.point_focus, rotation[0])
            self.screen_plane.init_pervec(self.screen_vec)
            self.screen_plane.set_d(self.point_screen)

            self.h_vec.rot_xz(self.point_focus, rotation[0])

            self.point_screen.rot_yz(self.point_focus, rotation[1])
            self.corner_topleft.rot_yz(self.point_focus, rotation[1])

            self.screen_vec.rot_yz(self.point_focus, rotation[1])
            self.screen_plane.init_pervec(self.screen_vec)
            self.screen_plane.set_d(self.point_screen)

            self.h_vec.rot_yz(self.point_focus, rotation[1])
        
    def projection(self, face):
        polygon = []

        #print(face)

        for point in face:
            self.point_to_focus_equation.init_points(point, self.point_focus)
            self.poi = self.screen_plane.intersect_linearequation(self.point_to_focus_equation)

            polygon.append(self.poi)
            #self.poi.print()

        return polygon

    def print(self):
        print("")