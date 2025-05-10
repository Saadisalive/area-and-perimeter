import math

class circle:
    def __init__(self,radius):

        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius**2
    
    def calculate_circle_parameter(self):
        return 2 * math.pi * self.radius
    
radius = int(input("Input the radius of a circle :"))

circle = circle(radius)

area = circle.calculate_circle_area()

parimeter = circle.calculate_circle_parameter()

print("Area of a circle :",area)
print("Perimeter of the circle :",parimeter)