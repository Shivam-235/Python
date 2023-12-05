class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printName(self):
        print(self.name)
class Student(Person):
    def __init__(self,name, age, regno):
        self.regno = regno
        super().__init__(name, age)
    def printRegNo(self):
        print(self.regno)
s1 = Student("Rahul", 19, 101)
s1.printRegNo()
s1.printName()