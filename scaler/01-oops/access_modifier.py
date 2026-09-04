class Student:
    def __init__(self, name, psp):
        self.name = name
        self.psp = psp
        self.__age = 40
        self._email = "aditya@hello.com"

    def print_name(self):
        print(f"Hello {self.name} !")
    def print_age(self):
        print(f"this is my age {self.__age}")

aditya = Student("aditya", 90)
rohit = Student("rohit", 91)

aditya.print_name()
rohit.print_name()

# public access modifier
print(aditya.name)

# private
# print(aditya.__age)
print(aditya._Student__age) # name mangling way to call private variable
aditya.print_age()



# protected
print(aditya._email)