from math import sqrt
from graph import *
import pygame

def toVector2(list):
    new_list = []
    for item in list:
        new_list.append(pygame.math.vector2)

def vec_cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def vec_subtract(a, b):
    c = [a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2]]
    return c

def vec_intersect_plane(a, x, i):
    t = -(a[0] * i[0] + a[1] * i[1] + a[2] * i[2] - a[3]) / (a[0] * x[0] + a[1] * x[1] + a[2] * x[2])
    p = [t * x[0] + i[0], t * x[1] + i[1], t * x[2] + i[2]]
    return p

def vec_make_points(a, b):
    vec = Vector_3()
    vec.init_points(a, b)
    return vec

def vec_make_raw(x, y, z):
    vec = Vector_3()
    vec.init_raw(x, y, z)
    return vec

def plane_make_vecnpoint(vec, p):
    plane = Plane()
    plane.init_pervec(vec)
    plane.set_d(p)
    return plane

def linearequation_make(p1, p2):
    l = Linear_Equation()
    l.init_points(p1, p2)
    return l

def linearequation_make_vec(vec, p):
    l = Linear_Equation()
    l.init_vec(vec, p)
    return l

def delta_2d_pos(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]