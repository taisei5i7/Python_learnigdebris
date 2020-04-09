class Shape:
    shape_list = []

    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.shape_list.append((self.length, self.width))

    def print_size(self):
        print("{} by {}".format(self.length, self.width))

s1 = Shape(20, 30)
s2 = Shape(50, 60)
s3 = Shape(40, 80)
print(Shape.shape_list)

    
class Square:

    def __init__(self, l):
        self.length = l

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

re = Square(33)
print(re)


class unsuit:

    def __init__(self):
        self.name = "S"
        self.sex = "male"

suit = unsuit()
same_suit = suit
print(suit is same_suit)


def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
print(compare("a", "a"))
