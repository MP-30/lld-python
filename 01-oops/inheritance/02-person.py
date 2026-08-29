class Person:
    name: str
    age: int
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[0]
        else:
            raise IndexError("Only 2 args are permitted")