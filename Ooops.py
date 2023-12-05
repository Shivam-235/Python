#Program using classes and objects
class student:
    def __init__(self,name,age,school):
        self.name=name
        self.age=age
        self.school=school
    def printDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("School:",self.school)
    def printWish(self):
        print("Good Morning")
#Now we are creating objects
stud1 = student("Raj",20,"CSE")
#You can access the attributes of the object using the dot operator
print('Accessing name of student:',stud1.name)
#you can call the methods of the object using the dot operator
stud1.printDetails()
stud2 = student("Ravi",21,"ECE")
stud2.printDetails()
stud2.printWish()