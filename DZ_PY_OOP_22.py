import math


class Sphere:

    def __init__(self, r=0, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, r):
        self.r = r

    def get_volume(self):
        return (self.r ** 3) * math.pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * math.pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.r ** 2:
            return True
        return False


sp1 = Sphere()
sp1.set_radius(0.6)
print("get_radius: ", sp1.get_radius())
print("get_volume: ", sp1.get_volume())
print("get_square: ", sp1.get_square())
print("get_center: ", sp1.get_center())
print("is_point_inside:(0, 1.5, 0):", sp1.is_point_inside(0, -1.5, 0))
sp1.set_radius(1.6)
print("get_radius: ", sp1.get_radius())
print("is_point_inside: (0, 1.5, 0):", sp1.is_point_inside(0, -1.5, 0))
