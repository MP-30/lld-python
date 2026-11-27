class University:
    def course(self):
        print("Has 4 course")

class Institute_A(University):
    def classes(self):
        print("classes are running")
    def students(self):
        print("Students are learning")

class Institute_B(University):
    def classes(self):
        print("Classes are happening")
    def breaks(self):
        print("Breaks hapens between the classes")

A = Institute_A()
A.course()