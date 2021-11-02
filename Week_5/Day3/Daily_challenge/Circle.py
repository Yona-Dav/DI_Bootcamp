import math
import turtle

class Circle:
    circles = []
    def __init__(self):
        print(''' 
            1. Diameter
            2. Radius
            ''')
        ans = input('Which one to you want to input. Enter a number ')
        if ans=='1':
            self.diameter = int(input('Enter diameter '))
            self.radius = self.diameter/2
        elif ans=='2':
            self.radius = int(input('Enter the radius '))
        self.circles.append(self.radius)
          
    
    def circle_area(self):
        self.aera = math.pi*self.radius**2
        print(self.aera)
    
    def draw_circle(self):
        t = turtle.Turtle()
        print(t.circle(self.radius))
    
    def __add__(self,other):
        return self.radius + other.radius
    
    def __gt__(self,other):
        if self.radius > other.radius:
            return True
        elif self.radius < other.radius:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def list_sorted(self):
        return sorted(self.circles)

circle1 = Circle()
circle1.circle_area()
circle1.draw_circle()

circle2 = Circle()
circle2.circle_area()
circle2.draw_circle()

print(circle2+circle1)
print(circle1>circle2)
print(circle1==circle2)
print(circle2.list_sorted())
        
