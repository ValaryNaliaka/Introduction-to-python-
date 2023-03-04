#Area and perimeter of a circle
class Circle:
    def __init__(self,radius):
#radius=int(input("enter the radius"))
        self.radius=radius
    def area(self):
        area=(3.142*self.radius*self.radius)
        print("area of the circle",area)
    def perimeter(self):
        perimeter=(3.142*2*self.radius)
        print("perimeterof the circle",perimeter)
cir=Circle(7)
cir.area()
cir.perimeter()