class Shape:

    def what_am_i(self):
       return print("I am shape.")


class Rectangle(Shape):

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def perimeter_rec(self):
        return self.length * 2 + self.width * 2

    
    
class Square(Shape):

    def __init__(self, sl, sw):
        self.lengthsq = sl
        self.widthsq = sw

    def perimeter_squ(self):
        return self.lengthsq * 2 + self.widthsq * 2
    
   

rec = Rectangle(20, 30)
print(rec.perimeter_rec())

squ = Square(30, 40)
print(squ.perimeter_squ())
    
rec.what_am_i()
squ.what_am_i()
