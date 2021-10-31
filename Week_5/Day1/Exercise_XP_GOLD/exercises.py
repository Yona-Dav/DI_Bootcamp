# Exercise 1 : Geometry

# Write a class called Circle that receives a radius as an argument (default is 1.0).

import math
from operator import ne

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return self.radius/2 * math.pi

    def area(self):
        return self.radius**2 * math.pi

    def definition(self):
        print('A circle is ....')

circle = Circle(4)
print(circle.radius)
print(circle.area())
print(circle.perimeter())
circle.definition()


# Exercise 2 : Custom List Class
import random
class MyList:
    def __init__(self,list_letter):
        self.letter = list_letter
    
    def reversed_list(self):
        return self.letter[::-1]
    
    def sorted_list(self):
        return sorted(self.letter)

    def second_list(self):
        second_list = [random.randint(1,100) for x in range(len(self.letter))]
        return second_list

new_list = MyList([7,85,9,12,45,68,15,25,8,17,98])
print(new_list.reversed_list())
print(new_list.sorted_list())
print(new_list.second_list())




