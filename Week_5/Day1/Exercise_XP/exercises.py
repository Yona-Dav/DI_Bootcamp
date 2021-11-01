# Exercise 1: Cats

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate three Cat objects using the code provided above.
data_cats = [('rex',34),('bubbles',12),('misti',8)]
cats = [Cat(*data) for data in data_cats]

# Create a function that finds the oldest cat and returns the cat.

def oldest_cat(cat_list):
    cat = sorted(cat_list, key=lambda cat:cat.age)[-1]
    return cat

oldest = oldest_cat(cats)
print(oldest.name, oldest.age)

# def oldest_longer(cat_list):
#     age = cat_list[0].age
#     current_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age>age:
#             current_cat = cat
#     return current_cat

# oldest = oldest_longer(cats)
# print(oldest.name, oldest.age)


# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')



davids_dog = Dog('Rex', 50)
print(f"The dog's name is {davids_dog.name} and his height is {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 120)
print(f"The dog's name is {sarahs_dog.name} and his height is {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

dog_list = [davids_dog,sarahs_dog]

def bigger_dog(dog_list):
    dog = sorted(dog_list, key=lambda dog:dog.height)[-1]
    return dog

bigger = bigger_dog(dog_list)
print(bigger.name, bigger.height)


# Exercise 3 : Who’s The Song Producer?

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo

from collections import defaultdict 

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        self.new_animal = new_animal
        if self.new_animal not in self.animals:
            self.animals.append(self.new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):    
        groups=defaultdict(list)
        for animal in sorted(self.animals):
            groups[animal[0]].append(animal)
        animal_sorted = sorted(groups.values())
        self.index_animal = {}
        for index, animal in enumerate(animal_sorted):
            if len(animal)==1:
                self.index_animal[index+1] = animal[0]
            else:
                self.index_animal[index+1]=animal

    def get_groups(self):
        for values in self.index_animal.values():
            print(values)
        print(self.index_animal)
        



ramat_gan_safari = Zoo('Safari')
ramat_gan_safari.add_animal('Chicken')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Emu')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Monkey')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Bear')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()


# other way to sort_animals
    # def sort_animals(self):
    #     '''Create a method called sort_animals that sorts the animals
    #      alphabetically and groups them together based on their first letter.'''
    #     animals_lists = []
    #     for animal in sorted(self.animals):
    #         print('current animal:', animal)
    #         if not animals_lists:
    #             animals_lists.append([animal])
                
    #         else:
    #             print(f"current animal first letter: {animal[0]}")
    #             print(f"last list: {animals_lists[-1]}")
    #             print(f"first object in last list: {animals_lists[-1][0]}")
    #             print(f"first letter of first object in last list: {animals_lists[-1][0][0]}")
    #             if animal[0] == animals_lists[-1][0][0]:
    #                 print('matches last object')
    #                 animals_lists[-1].append(animal)
    #             else:
    #                 animals_lists.append([animal])