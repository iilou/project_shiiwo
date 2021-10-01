from math import *


class Plane():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def init_pervec(self, vec):
        self.a = vec.x
        self.b = vec.y
        self.c = vec.z

    def set_d(self, p):
        self.d = self.a * p.x + self.b * p.y + self.c * p.z

    def intersect_linearequation(self, l):
        t = -(self.a * l.x + self.b * l.y + self.c * l.z - self.d) / (self.a * l.a + self.b * l.b + self.c * l.c)
        round(t, 8)
        poi = Point_3(t * l.a + l.x, t * l.b + l.y, t * l.c + l.z)
        return poi

    def print(self):
        print(str(self.a), str(self.b), str(self.c), str(self.d)) 

class Vector_3():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def init_points(self, p1, p2):
        self.x = p1.x - p2.x
        self.y = p1.y - p2.y
        self.z = p1.z - p2.z

    def init_raw(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def opposite(self, v):
        if not v.x == 0:
            if v.x < 0 & self.x > 0: return True
            if v.x > 0 & self.x < 0: return True
        if not v.y == 0:
            if v.y < 0 & self.y > 0: return True
            if v.y > 0 & self.y < 0: return True
        if not v.z == 0:
            if v.z < 0 & self.z > 0: return True
            if v.z > 0 & self.z < 0: return True

    def length_vec(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) 

    def unit_vec(self):
        len = self.length_vec()
        self.x /= len
        self.y /= len
        self.z /= len

    def dot_raw(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def rot_xz(self, o, theta):
        theta = radians(theta)

        nx = cos(theta) * (self.x - o.x) - sin(theta) * (self.z - o.z) + o.x
        nz = sin(theta) * (self.x - o.x) + cos(theta) * (self.z - o.z) + o.z

        self.x = nx
        self.z = nz

    def rot_yz(self, o, theta):
        theta = radians(theta)
        ny = cos(theta) * (self.y - o.y) - sin(theta) * (self.z - o.z) + o.y
        nz = sin(theta) * (self.y - o.y) + cos(theta) * (self.z - o.z) + o.z

        self.y = ny
        self.z = nz

    def print(self):
        print(str(self.x), str(self.y), str(self.z))


class Linear_Equation():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def init_raw(self, a, b, c, x, y, z):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
        self.z = z

    def init_points(self, p1, p2):
        self.a = p1.x - p2.x
        self.b = p1.y - p2.y
        self.c = p1.z - p2.z

        self.x = p1.x
        self.y = p1.y
        self.z = p1.z

    def get_vec(self):
        v = Vector_3()
        v.init_raw = (self.a, self.b, self.c)
        return v

    def set_pos(self, p):
        self.x = p.x
        self.y = p.y
        self.z = p.z

    def intersect_linearequation(self, l):
        #x = ((self.x * l.a) + (l.x * self.a)) / (l.a - self.a)
        #y = ((self.y * l.b) + (l.y * self.b)) / (l.b - self.b)
        
        x = 0
        if l.x - self.x == 0: x = self.x
        else: x = ((self.x * l.a) - (l.x * self.a)) / (l.a - self.a)

        y = 0
        if l.b - self.b == 0:  
            y = self.y
        else: y = ((self.y * l.b) - (l.y * self.b)) / (l.b - self.b)

        z = 0
        if l.c - self.c == 0: z = self.z
        else: z = ((self.z * l.c) - (l.z * self.c)) / (l.c - self.c)

        return Point_3(x, y, z)

    def init_vec(self, vec, p):
        self.a = vec.x
        self.b = vec.y
        self.c = vec.z

        self.x = p.x
        self.y = p.y
        self.z = p.z

    def get_copy(self):
        l = Linear_Equation()
        l.init_raw(self.a, self.b, self.c, self.x, self.y, self.z)
        return l

    def move(self, arr):
        self.x += arr[0]
        self.y += arr[1]
        self.z += arr[2]

    def print(self):
        print(str(self.a), str(self.b), str(self.c), str(self.x), str(self.y), str(self.z))

class Point_3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, arr):
        self.x += arr[0]
        self.y += arr[1]
        self.z += arr[2]

    def get_copy(self):
        return Point_3(self.x, self.y, self.z)

    def rot_xz(self, o, theta):
        nx = cos(theta) * (self.x - o.x) - sin(theta) * (self.z - o.z) + o.x
        nz = sin(theta) * (self.x - o.x) + cos(theta) * (self.z - o.z) + o.z

        self.x = nx
        self.z = nz

    def rot_yz(self, o, theta):
        theta = radians(theta)
        ny = cos(theta) * (self.y - o.y) - sin(theta) * (self.z - o.z) + o.y
        nz = sin(theta) * (self.y - o.y) + cos(theta) * (self.z - o.z) + o.z

        self.y = ny
        self.z = nz

    def print(self):
        print(str(self.x), str(self.y), str(self.z))

    