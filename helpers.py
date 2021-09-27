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
    c = [b[0] - a[0],
        b[1] - a[1],
        b[2] - a[2]]
    return c

def length_3(a):
    return sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)