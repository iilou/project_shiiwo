from objects import Object, Camera

def vector_subtract(vec1, vec2):
    vec_final = []

    for i in range(vec1):    
    return vec_final


class World():
    def __init__(self, camera):
        self.objects = []
        self.camera = camera

    def addObject(self, object):
        self.objects.append(object)

    def addCamera(self, pos, size, dist, rot):
        self.camera.pos = pos
        self.camera.size = size
        self.camera.dist = dist
        self.camera.rot = rot


    def getImage():
        poly = []
        vec = vector_subtract(poly, [])

        return []
    

#camera = Camera([],[],0,[])
#shiiwo = World(camera)

#camera.pos = [5,5,5]
#shiiwo.camera.print()

#points = [[1, 5], [6, 2], [8, 8], [1, 9]]
#object = Object(points, False)
#shiiwo.addObject(object)
#shiiwo.objects[0].print()