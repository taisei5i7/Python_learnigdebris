class Horse:
    def __init__(self, name, sex, owner):
        self.name = name
        self.sex = sex
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

Mike = Rider("Mike")
Uma = Horse("Uma","male",Mike)
print(Uma.owner.name)
