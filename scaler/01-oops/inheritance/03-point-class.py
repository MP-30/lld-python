class Point:
    def __init__(self, x: float| int, y: float | int ):
        self.x = x
        self.y = y
    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

p1 = Point(10,12)
p2 = Point(10,12)
print(p1.__eq__(p2))