# Exercise 3 : Dogs Domesticated

from Exercise1_2 import Dog
import random

class PetDog(Dog):
    def __init__(self,name, age, weight, trained=False):
        super().__init__(name,age,weight)
        self.trained = trained
    
    def train(self):
        self.trained = True
        return super().bark()
    
    def play(self,*args):
        print(f'{self.name}, ',end='')
        for dog in args:
            print(f'{dog.name}, ',end='')
        print(end='')
        return 'all play together'

    def do_a_trick(self):
        order = [f'{self.name} does a barrel roll',f'{self.name} stands on his back legs',f'{self.name} shakes your hand',f'{self.name} plays dead']
        print(random.choice(order))
    
dog1 = PetDog('Rox', 15, 50)
dog2 = PetDog('Milou',12,35)
dog3 = PetDog('Cho',8,15)
print(dog1.train())
print(dog1.play(dog2,dog3))
dog1.do_a_trick()
dog2.do_a_trick()