# Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = {}

for k,v in zip(keys,values):
    my_dict[k]=v

print(my_dict)

# Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# family={}
# for num in range(0,3):
#     person = input('Enter a name')
#     age = int(input(f'Enter the age of {person}'))
#     family[person]=age
# print(family)

total_cost = 0
for person, age in family.items():
    if age<3:
        price = 0
    elif 2<age<13:
        price = 10
        total_cost +=price
    else:
        price=15
        total_cost +=price
    print(f'{person} has to paid ${price}')
print(f'The total cost is ${total_cost}')

# Exercise 3: Zara

brand = {}
keys = ['name', 'creation_date', 'creator_name', 'type_of_clothes','international_competitors','number_stores']
values = ['Zara', 1975, 'Amancio Ortega Gaona', ['men','women','children','home'],['Gap','h&m','Benetton'], 7000]

for k,v in zip(keys,values):
    brand[k] = v

brand['major_color']={}
brand['major_color']['France']='blue'
brand['major_color']['Spain']='red'
brand['major_color']['US']=['pink','green']


brand['number_stores']=2 #Change the number of stores to 2.



print('The clients of zara are:')
for clients in brand['type_of_clothes']:
    print(clients)

brand['country_creation'] = 'Spain'

for k,v in brand.items():
    if 'international_competitors' in k:
        brand['international_competitors'].append('Desigual')


del brand['creation_date'] #Delete the information about the date of creation.

print(brand['international_competitors'][-1]) # Print the last international competitor

print(brand['major_color']['US']) #Print the major clothes colors in the US

print(len(brand)) #Print the amount of key value pairs

print(brand.keys()) #Print the keys of the dictionary.

more_on_zara = {
    'creation_date':1975,
    'number_stores':10000
}

brand.update(more_on_zara) #add the information from the dictionary more_on_zara to the dictionary brand.

print(brand['number_stores']) #it changes the value to the added value


# Exercise 4 : Disney Characters

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

disney_users_A ={}
disney_users_B ={}
disney_users_C ={}

for index, name in enumerate(users):
    disney_users_B[index]=name
    disney_users_A[name]=index

for index, name in enumerate(sorted(users)):
    disney_users_C[name]=index

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)

disney_users_D={} #The characters, which names contain the letter “i”.
users2 = []
for name in users:
    if 'i' in name:
        users2.append(name)
        for index, name in enumerate(users2):
            disney_users_D[name]=index
print(disney_users_D)
        
        
disney_users_E={} #he characters, which names start with the letter “m” or “p”.
users3 = []
for name in users:
    if name[0]=='M' or name[0]=="P":
        users3.append(name)
        for index, name in enumerate(users3):
            disney_users_E[name]=index
print(disney_users_E)
