class Object():
    def __init__(self, data, isRound):
        if not isRound:
            self.data = data

    def print(self):
        for i in self.data:
            print(i)

#square = Object([[1, 2, -1], [2, 3, 1], [8, -2, 3]], False)
#square.print()


class Camera():

    #position - point reference connects to plane    size - width height of plane   dist - distance from point to plane     rot - angle from [1 0 0]
    def __init__(self, pos, size, dist, rot):
        self.pos = pos
        self.size = size
        self.dist = dist
        self.rot = rot

    def print(self):
        print(str(self.pos), " ", str(self.size), " ", self.dist, " ", str(self.rot))