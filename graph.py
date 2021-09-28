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

    def intersect_vec(self, vec):
        return vec

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

class Linear_Equation():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def init_points(self, p1, p2):
        self.a = p1.x - p2.x
        self.b = p1.y - p2.y
        self.c = p1.z - p2.z

        self.d = self.a * p1.x + self.b * p1.y + self.c * p1.z



class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z