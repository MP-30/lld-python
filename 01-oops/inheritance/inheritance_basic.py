class Animal:
    def run(self):
        print ( "run at 4 legs")

class Dog(Animal):
    def eating(self):
        print("Dog is eating")
    def run(self):
        print("runs on legs")

class Tiger(Animal):
    def eating(self):
        print("Tiger is eating")

# T = Tiger()
# T.run()
# D = Dog()
# D.run()


# multiple inheritance
class Human:
    def sleep(self):
        print ('human can sleep')
class Man:
    def sleep(self):
        print ('man can sleep')

class Boy(Human, Man):
    def run(self):
        print('Boy can run')

# B = Boy()
# B.run()
# B.sleep()
# Man.sleep(Boy)

# multi level inheritance

class Grandfather:
    ...

class Father:
    ...
class Child:
    ...
class Grandchild:
    ...

# =========

# Hierarchical inherirance
class Sachin:
    ...
class Dhoni:
    ...
class Yovraj:
    ...
class Kolhi:
    ...
class Rohit:
    ...
class Yzi:
    ...
class Hardik:
    ...

# Hybrid inheritance