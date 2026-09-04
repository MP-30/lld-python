class Student:
    def __init__(self, name, id, age, batchID, email, attendance, psp):
        self.name = name
        self.age = age
        self.batchID = batchID
        self.email = email
        self.id = id
        self.attendance = attendance
        self.psp = psp

    def solve_assignment(self):
        print(f"Person with {self.name} name, id {self.id} solved psps is {self.psp}" )

    def attend_class(self):
        print(f"Person with {self.email} name, batch id {self.batchID} have this attendance {self.attendance}")

    def contest_attent(self):
        print(f"{self.name} contest attendance is {self.attendance}")

naman = Student("Naman", 101, 22, "Batch-01", "adti@xyz.com", 98, 95)
naman.solve_assignment()
naman.attend_class()
naman.contest_attent()