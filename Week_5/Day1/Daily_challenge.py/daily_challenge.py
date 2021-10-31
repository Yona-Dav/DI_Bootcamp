#  Old MacDonald’s Farm

class Farm:
    def __init__(self,name):
        self.name = name
        self.animals = {}

    def add_animal(self,animal, quantity=1):
        if animal not in self.animals:
            self.animals[animal]=quantity
        else:
            self.animals[animal] += quantity
        
    def get_info(self):
        print(f'{self.name}\'s name\n')
        for animal, qtt in self.animals.items():
            print(f'{animal} : {qtt}')
        print('')
        return '     E-I-E-I-0!'

    def get_animal_types(self):
        self.new_list = []
        for animal in self.animals:
            self.new_list.append(animal)
        self.sorted_list = sorted(self.new_list)
        return self.sorted_list
    
    def get_short_info(self):
        list_animals = self.get_animal_types()
        print('McDonald’s farm has ',end='')
        for i in range(len(list_animals)-1):
            print(f'{list_animals[i]}s, ', end='')
        return(f'and {list_animals[-1]}s.')




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())