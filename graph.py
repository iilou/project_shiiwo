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
        t = -(self.a * l.x + self.b * l.y + self.c * l.z - self.d) / (self.a * l.a + self.b * l.b + self.c + l.c)
        poi = Point_3(t * l.a + l.x, t * l.b + l.y, t * l.c + l.z)
        return poi

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
        x = ((self.x * l.a) + (l.x * self.a)) / (l.a - self.a)
        y = ((self.y * l.b) + (l.y * self.b)) / (l.b - self.b)
        z = ((self.z * l.c) + (l.z * self.c)) / (l.c - self.c)

        return Point_3(x, y, z)

    def init_vec(self, vec, p):
        self.a = vec.x
        self.b = vec.y
        self.c = vec.z

        self.x = p.x
        self.y = p.y
        self.z = p.z

class Point_3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    