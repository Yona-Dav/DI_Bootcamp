# Exercise 1 : Family

class Family:
    def __init__(self,members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **new_member):
        self.members.append(new_member)
        print(f'Congratulation to the {self.last_name} family')

    def is_18(self,name):
        for member in self.members:
            if member['name']==name:
                    if member['age']>18:
                        return True
                    else:
                        return False

    def all_members(self):
        for member in self.members:
            print(f"{member['name']}, {member['age']} years old, {member['gender']}, is_child:{member['is_child']}")


people = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

family1 = Family(people,'David')
family1.born(name='Lea',age=0,gender='Female',is_child=True)
print(family1.is_18("Lea"))
print(family1.is_18("Michael"))
family1.all_members()


# Exercise 2 : TheIncredibles Family

class TheIncredibles(Family):

    def use_power(self,name):
        for member in self.members:
            if member['name']==name:
                if member['age']>18:
                    print(member['power'])
                else:
                    raise Exception("He has under 18 years old, he cannot use his power")
    
    def incredible_presentation(self):
        for member in self.members:
            print(member['incredible_name'], member['power'])
    

people2 = [
    {'name':'Robert','age':39,'gender':'Male','is_child':False, 'power': 'superhuman strength', 'incredible_name':'Mr. Incredible'},
    {'name':'Helen','age':35,'gender':'Female','is_child':False, 'power': 'elastic', 'incredible_name':'Elastigirl'},
    {'name': 'Violet', 'age': 14, 'gender': 'Female', 'is_child': True,'power': 'invisibility', 'incredible_name':'Visea'}
]

incredible_family = TheIncredibles(people2, 'Parr')
# incredible_family.use_power('Sarah')
#incredible_family.use_power('Lea')
incredible_family.all_members()
incredible_family.incredible_presentation()
incredible_family.born(name='Baby Jack',age=0,gender='Male',is_child=True, power='Unknown Power',incredible_name='unknown')
incredible_family.all_members()
incredible_family.incredible_presentation()