class Points:
    def __init__(self, x:float  , y: float  ):
        self.x = x
        self.y = y
    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __noteq__(self,other):
        if self.x == other.x and self.y == other.y:
            return False
        else:
            return True

p1 = Points(1,2)
p2 = Points(4,4)
print(p1.__eq__(p2))
print(p1.__noteq__(p2))
print(p1 == p2)

import copy
d = 12
copy.deepcopy(d)