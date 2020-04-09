import math

class Apple():

    def __init__(self, c, w, s, d):
        self.color = c
        self.weight = w
        self.sweet = s
        self.diameter = d
        print("Apple is cleated.")
        
class Circle():

    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi
a_circle = Circle(4)
print(a_circle.area())

class Rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area_rec(self):
        return self.length * self.width
a_rectangle = Rectangle(5, 10)
print(a_rectangle.area_rec())

class Triangle():

    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area_tri(self):
        return self.base * self.height / 2
a_triangle = Triangle(20, 10)
print(a_triangle.area_tri())

class Hexagon():

    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.perimeter())



