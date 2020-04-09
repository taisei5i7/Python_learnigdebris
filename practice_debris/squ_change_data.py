import math

class Square():

    def __init__(self, l):
        self.length = l

    def perimeter(self):
        return self.length*4

    def change_data(self, n):
        self.length += n

squ = Square(10)
print(squ.perimeter())

squ.change_data(5)
print(squ.perimeter())

    

