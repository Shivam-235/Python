#Method Overriding
#Base Class
class Shape:
    def setDimensions(self, sides):
        self.sides = sides
    def printShape(self):
        if self.sides == 3:
            print("Triangle")
        elif self.sides == 4:
            print("square")
        else:
            print("Invalid Shape")
    def printArea(self):
        print("Area Not Defined")
#Derived Class
class Square(Shape):
    def setDimensions(self, side):
        self.side = side
        self.shape = "square"
    def printShape(self):
        print('output from overridden method', self.shape)
#create object of derived class
o1 = Square()
o1.setDimensions(5)
o1.printShape()
o1.printArea()