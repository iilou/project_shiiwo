from math import sqrt
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

def length_3(a):
    return sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)

def vec_intersect_plane(a, x, i):
    t = -(a[0] * i[0] + a[1] * i[1] + a[2] * i[2] - a[3]) / (a[0] * x[0] + a[1] * x[1] + a[2] * x[2])
    p = [t * x[0] + i[0], t * x[1] + i[1], t * x[2] + i[2]]
    return p

def vec_make(a, b):
    return [a[0] - b[0],
            a[1] - b[1],
            a[2] - b[2]]